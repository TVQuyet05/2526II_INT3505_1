from flask import Flask, jsonify, request
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f0x8qxwq9kuap19apk6v2gc1qbnsjv'

# Giả lập Database Users
users_db = {
    "admin": "password123",
    "user1": "pass456"
}

# Decorator để bảo vệ các route cần JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # Lấy token từ header Authorization: Bearer <token>
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(" ")[1]
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            # Giải mã token
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            # Kiểm tra user trong token (nếu cần)
            current_user = data['username']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401
            
        return f(current_user, *args, **kwargs)
    
    return decorated

@app.route('/login', methods=['POST'])
def login():

    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing username or password'}), 400

    username = data.get('username')
    password = data.get('password')

    if username in users_db and users_db[username] == password:
        # Tạo JWT token
        token = jwt.encode({
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({'token': token})

    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/protected', methods=['GET'])
@token_required
def protected_route(current_user):
    return jsonify({
        'message': f'Hello {current_user}, this is a protected route!',
        'status': 'allowed'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)
