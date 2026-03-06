"""
Version 1: Client-Server Architecture
- Server (Flask) xử lý logic và phục vụ dữ liệu
- Client (HTML/JS) chỉ hiển thị và tương tác với người dùng
- Phân tách rõ ràng giữa client và server
"""

from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route phục vụ trang HTML (Client)
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint đơn giản - Server trả về dữ liệu
@app.route('/api/hello')
def hello():
    return jsonify({
        'message': 'Hello from Server!',
        'status': 'success'
    })

# API endpoint - Server trả về thời gian hiện tại
@app.route('/api/time')
def get_time():
    from datetime import datetime
    return jsonify({
        'time': datetime.now().strftime('%H:%M:%S'),
        'date': datetime.now().strftime('%Y-%m-%d')
    })

if __name__ == '__main__':
    print("=== Client-Server Demo ===")
    print("Server đang chạy tại: http://localhost:5000")
    print("Client truy cập: http://localhost:5000")
    print("API endpoints:")
    print("  - GET /api/hello")
    print("  - GET /api/time")
    app.run(debug=True, port=5000)
