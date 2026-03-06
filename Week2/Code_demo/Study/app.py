"""
Version 1: Client-Server Architecture
- Server (Flask) xử lý logic và phục vụ dữ liệu
- Client (HTML/JS) chỉ hiển thị và tương tác với người dùng
- Phân tách rõ ràng giữa client và server
"""

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

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

if __name__ == '__main__':
    print("=== 📚 Library API Server ===")
    print("Server đang chạy tại: http://localhost:5000")
    print("\nAPI endpoints:")
    print("  - GET /api/books          : Lấy tất cả sách")
    print("  - GET /api/books/<id>     : Lấy sách theo ID")
    print("  - GET /api/books/category/<name> : Lấy sách theo danh mục")
    print("  - GET /api/books/available: Lấy sách có sẵn")
    print("  - GET /api/stats          : Thống kê thư viện")
    app.run(debug=True, port=5000)
