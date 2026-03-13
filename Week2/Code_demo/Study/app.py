"""
Version 1: Client-Server Architecture
- Server (Flask) xử lý logic và phục vụ dữ liệu
- Client (HTML/JS) chỉ hiển thị và tương tác với người dùng
- Phân tách rõ ràng giữa client và server
"""

from flask import Flask, render_template, jsonify, request
import uuid

app = Flask(__name__)

# ==================== DATA MẪU CHO SESSION ====================
USERS = {
    "admin": {"password": "123", "role": "admin"},
    "user": {"password": "123", "role": "user"}
}
SESSIONS = {}

# ==================== DỮ LIỆU SÁCH THƯ VIỆN ====================
books = [
    {
        "id": 1,
        "title": "Lập trình Python cơ bản",
        "author": "Nguyễn Văn A",
        "year": 2023,
        "category": "Công nghệ",
        "available": True
    },
    {
        "id": 2,
        "title": "Cấu trúc dữ liệu và giải thuật",
        "author": "Trần Văn B",
        "year": 2022,
        "category": "Công nghệ",
        "available": True
    },
    {
        "id": 3,
        "title": "Nhà giả kim",
        "author": "Paulo Coelho",
        "year": 2020,
        "category": "Văn học",
        "available": False
    },
    {
        "id": 4,
        "title": "Đắc nhân tâm",
        "author": "Dale Carnegie",
        "year": 2019,
        "category": "Kỹ năng sống",
        "available": True
    },
    {
        "id": 5,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "year": 2021,
        "category": "Công nghệ",
        "available": True
    }
]

# ==================== ROUTES ====================

# Route phục vụ trang HTML (Client)
@app.route('/')
def index():
    return render_template('index.html')

# API: Lấy tất cả sách
@app.route('/api/books', methods=['GET'])
def get_all_books():
    return jsonify({
        'success': True,
        'count': len(books),
        'data': books
    })

# API: Lấy sách theo ID
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify({
            'success': True,
            'data': book
        })
    return jsonify({
        'success': False,
        'message': 'Không tìm thấy sách'
    }), 404

# API: Tìm sách theo category
@app.route('/api/books/category/<category>', methods=['GET'])
def get_books_by_category(category):
    filtered = [b for b in books if b['category'].lower() == category.lower()]
    return jsonify({
        'success': True,
        'count': len(filtered),
        'data': filtered
    })

# API: Lấy sách có sẵn
@app.route('/api/books/available', methods=['GET'])
def get_available_books():
    available = [b for b in books if b['available']]
    return jsonify({
        'success': True,
        'count': len(available),
        'data': available
    })

# API: Thống kê thư viện
@app.route('/api/stats', methods=['GET'])
def get_stats():
    total = len(books)
    available = len([b for b in books if b['available']])
    categories = list(set(b['category'] for b in books))
    
    return jsonify({
        'success': True,
        'data': {
            'total_books': total,
            'available_books': available,
            'borrowed_books': total - available,
            'categories': categories
        }
    })

# ==================== AUTHENTICATION (SESSION DEMO) ====================
def err(code, message, status_code):
    return jsonify({"error": code, "message": message}), status_code

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    # 1. Lấy dữ liệu từ users
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    # 2. Validate dữ liệu đầu vào
    if not username or not password:
        return err("VALIDATION_ERROR", "username and password are required", 400)

    # 3. Kiểm tra user trong database (mock)
    user = USERS.get(username)
    if not user or user["password"] != password:
        return err("INVALID_CREDENTIALS", "Invalid username or password", 401)

    # 4. Tạo Session ID (SID) ngẫu nhiên
    sid = str(uuid.uuid4())
    
    # 5. Lưu thông tin user vào Server Session Storage
    SESSIONS[sid] = {"username": username, "role": user["role"]}

    # 6. Trả về SID cho client (qua Body và Cookie)
    resp = jsonify({
        "sessionId": sid, 
        "user": {"username": username, "role": user["role"]}
    })
    
    # Set cookie 'sid' (HttpOnly để bảo mật, chặn JS đọc)
    resp.set_cookie("sid", sid, httponly=True)
    
    return resp, 200

@app.route('/api/v1/profile', methods=['GET'])
def get_profile():
    # Demo cách dùng session để xác thực request
    sid = request.cookies.get("sid")
    if not sid or sid not in SESSIONS:
        return err("UNAUTHORIZED", "Please login first", 401)
    
    user_session = SESSIONS[sid]
    return jsonify({"message": "Welcome back!", "user": user_session})

@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    sid = request.cookies.get("sid")
    if sid and sid in SESSIONS:
        del SESSIONS[sid]
    
    resp = jsonify({"message": "Logged out successfully"})
    resp.set_cookie("sid", "", expires=0) # Xóa cookie
    return resp

if __name__ == '__main__':
    print("=== 📚 Library API Server ===")
    print("Server đang chạy tại: http://localhost:5000")
    print("\nAPI endpoints:")
    print("  - GET /api/books          : Lấy tất cả sách")
    print("  - GET /api/books/<id>     : Lấy sách theo ID")
    print("  - GET /api/books/category/<name> : Lấy sách theo danh mục")
    print("  - GET /api/books/available: Lấy sách có sẵn")
    print("  - GET /api/stats          : Thống kê thư viện")
    print("  - POST /api/v1/auth/login  : Đăng nhập")
    print("  - GET /api/v1/profile      : Xem thông tin người dùng")
    print("  - POST /api/v1/auth/logout : Đăng xuất")
    app.run(debug=True, port=5000)
