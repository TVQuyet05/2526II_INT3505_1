from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# ==========================================
# 1. Ví dụ LỖI: Token Leakage
# ==========================================
@app.route('/api/vulnerable/profile', methods=['GET'])
def get_profile_vulnerable():
    # RỦI RO 1: Truyền token qua Query Parameter 
    # -> Dễ bị lộ qua URL, history trình duyệt, referer header
    token = request.args.get('token')
    
    # RỦI RO 2: Log toàn bộ token ra hệ thống 
    # -> Bất cứ ai có quyền xem log đều có thể chiếm đoạt token
    app.logger.info(f"VULNERABLE: User accessing with token: {token}")
    
    return jsonify({
        "message": "Profile data (vulnerable)",
        "token_received": token
    }), 200

# ==========================================
# 2. Ví dụ KHẮC PHỤC: Token Leakage
# ==========================================
@app.route('/api/secure/profile', methods=['GET'])
def get_profile_secure():
    # KHẮC PHỤC 1: Đọc từ Authorization header thay vì URL
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Unauthorized"}), 401
    
    token = auth_header.split(" ")[1]
    
    # KHẮC PHỤC 2: Che giấu (Masking) token trong log, chỉ in ra một phần nhỏ
    masked_token = f"***{token[-4:]}" if len(token) >= 4 else "***"
    app.logger.info(f"SECURE: User accessed profile with token ending in: {masked_token}")
    
    return jsonify({
        "message": "Profile data (secure)", 
        "masked_token": masked_token
    }), 200

if __name__ == '__main__':
    # Chạy ở port 5001 để tránh trùng lặp
    app.run(port=5001, debug=True)
