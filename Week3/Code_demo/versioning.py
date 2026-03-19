from flask import Flask, jsonify
import datetime

app = Flask(__name__)

# Dữ liệu mẫu
users_db = [
    {"id": 1, "name": "Nguyen Van A", "email": "a@example.com", "role": "admin"},
    {"id": 2, "name": "Tran Thi B", "email": "b@example.com", "role": "user"}
]

# ==================== API VERSION 1 ====================
@app.route('/api/v1/users', methods=['GET'])
def get_users_v1():
    """
    Version 1: Chỉ trả về danh sách tên (List of Strings)
    Cấu trúc đơn giản, ít thông tin.
    """
    # Transform data: chỉ lấy tên
    user_names = [user['name'] for user in users_db]
    
    return jsonify({
        "version": "v1",
        "users": user_names
    })

# ==================== API VERSION 2 (Mới hơn) ====================
@app.route('/api/v2/users', methods=['GET'])
def get_users_v2():
    """
    Version 2: Trả về danh sách object đầy đủ + Metadata
    Cấu trúc chi tiết, bao gồm id, email, role, và thông tin gói tin.
    """
    return jsonify({
        "meta": {
            "api_version": "2.0",
            "timestamp": datetime.datetime.now().isoformat(),
            "page": 1,
            "page_size": 10,
            "total_records": len(users_db)
        },
        "data": users_db,
        "links": {
            "self": "/api/v2/users",
            "next": "/api/v2/users?page=2"
        }
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
