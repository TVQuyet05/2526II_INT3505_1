from flask import Flask, jsonify, request
import base64

app = Flask(__name__)
app.json.sort_keys = False

# 1. Khởi tạo dữ liệu giả lập (50 cuốn sách)
books_db = [
    {
        "id": i,
        "title": f"Book Title {i}",
        "author": f"Author {i % 5}",
        "publishedYear": 2000 + (i % 25)
    } for i in range(1, 51)
]

@app.route('/')
def index():
    return jsonify({
        "message": "Welcome to Library Pagination Demo API",
        "endpoints": {
            "offset_limit": "/books/offset?offset=0&limit=5",
            "page_based": "/books/page?page=1&per_page=5",
            "cursor_based": "/books/cursor?cursor=eyJpZCI6IDV9&limit=5"
        }
    })

# --- 1. OFFSET/LIMIT PAGINATION ---
# Ưu điểm: Đơn giản, dễ hiểu. 
# Nhược điểm: Chậm khi offset lớn, dữ liệu có thể bị trùng/mất nếu có record mới chèn vào giữa.
@app.route('/books/offset', methods=['GET'])
def get_books_offset():
    offset = request.args.get('offset', default=0, type=int)
    limit = request.args.get('limit', default=5, type=int)
    
    data = books_db[offset : offset + limit]
    
    return jsonify({
        "type": "offset_limit",
        "offset": offset,
        "limit": limit,
        "total": len(books_db),
        "results": data
    })

# --- 2. PAGE-BASED PAGINATION ---
# Ưu điểm: Thân thiện với UI (hiển thị số trang 1, 2, 3...).
# Nhược điểm: Tương tự Offset/Limit (thực tế page-based là lớp vỏ bọc của offset/limit).
@app.route('/books/page', methods=['GET'])
def get_books_page():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=5, type=int)
    
    start = (page - 1) * per_page
    end = start + per_page
    data = books_db[start:end]
    
    total_pages = (len(books_db) + per_page - 1) // per_page
    
    return jsonify({
        "type": "page_based",
        "page": page,
        "per_page": per_page,
        "total_pages": total_pages,
        "total_results": len(books_db),
        "results": data
    })

# --- 3. CURSOR-BASED PAGINATION (SEEK METHOD) ---
# Ưu điểm: Hiệu năng cao (O(1)), tránh trùng lặp dữ liệu khi có record mới. Phù hợp Infinite Scroll.
# Nhược điểm: Không thể nhảy tới trang bất kỳ, chỉ có thể đi Tới hoặc Lùi.
@app.route('/books/cursor', methods=['GET'])
def get_books_cursor():
    cursor_str = request.args.get('cursor', default=None)
    limit = request.args.get('limit', default=5, type=int)
    
    last_id = 0
    if cursor_str:
        try:
            # Decode cursor (ở đây demo dùng Base64 của ID)
            decoded = base64.b64decode(cursor_str).decode('utf-8')
            last_id = int(decoded)
        except:
            return jsonify({"error": "Invalid cursor"}), 400

    # Lấy các record có ID lớn hơn last_id
    data = [b for b in books_db if b['id'] > last_id][:limit]
    
    # Tạo cursor mới từ ID cuối cùng trong list
    next_cursor = None
    if data:
        new_last_id = str(data[-1]['id'])
        next_cursor = base64.b64encode(new_last_id.encode('utf-8')).decode('utf-8')

    return jsonify({
        "type": "cursor_based",
        "limit": limit,
        "next_cursor": next_cursor,
        "results": data
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
