from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Mô phỏng cache bộ nhớ (trong thực tế thường sử dụng Redis)
nonce_cache = {}
MAX_TIME_DIFF = 300  # 5 phút (tính bằng giây)

# ==========================================
# 1. Ví dụ LỖI: Dễ bị Replay Attack
# ==========================================
@app.route('/api/vulnerable/transfer', methods=['POST'])
def transfer_money_vulnerable():
    data = request.json or {}
    token = request.headers.get('Authorization')
    
    # RỦI RO: Không có cơ chế kiểm tra thời gian hay id duy nhất (nonce).
    # Kẻ tấn công có thể "bắt" (sniff) gói tin HTTP này (nếu có cách vượt quyền hoặc nội bộ),
    # và gửi lại y hệt bao nhiêu lần tùy ý.
    # Logic hiện tại sẽ thực hiện lại hành động chuyển tiền lần nữa.
    
    return jsonify({
        "status": "success",
        "message": f"Transferred {data.get('amount', 0)} to {data.get('to', 'unknown')} successfully (Vulnerable)"
    }), 200


# ==========================================
# 2. Ví dụ KHẮC PHỤC: Chống Replay Attack 
# ==========================================
@app.route('/api/secure/transfer', methods=['POST'])
def transfer_money_secure():
    data = request.json or {}
    token = request.headers.get('Authorization')
    
    # Lấy Timestamp và Nonce (chuỗi ngẫu nhiên dùng 1 lần) từ header
    timestamp = request.headers.get('X-Timestamp')
    nonce = request.headers.get('X-Nonce')
    
    if not timestamp or not nonce:
        return jsonify({"error": "Missing X-Timestamp or X-Nonce headers"}), 400
        
    try:
        req_time = int(timestamp)
    except ValueError:
        return jsonify({"error": "Invalid X-Timestamp format"}), 400

    current_time = int(time.time())

    # KHẮC PHỤC 1: Kiểm tra Timestamp để chống Request quá hạn (stale request)
    if abs(current_time - req_time) > MAX_TIME_DIFF:
        return jsonify({"error": "Request expired / Invalid timestamp"}), 400

    # KHẮC PHỤC 2: Kiểm tra Nonce để chống gửi lại Request trong cùng thời gian hợp lệ
    # (Dọn dẹp cache giả lập để giải phóng bộ nhớ)
    keys_to_delete = [k for k, v in nonce_cache.items() if (current_time - v) > MAX_TIME_DIFF]
    for k in keys_to_delete:
        del nonce_cache[k]
    
    # Nếu nonce đã tồn tại -> Đây là gói tin cũ bị lặp lại!
    if nonce in nonce_cache:
        return jsonify({"error": "Replay attack detected! Nonce already used."}), 400
        
    # Ghi nhận nonce vào cache
    nonce_cache[nonce] = req_time

    # Lưu ý: Ở mức bảo mật cao hơn, bạn cần yêu cầu Client tạo chữ ký HMAC (Signature) 
    # cho (Payload + Timestamp + Nonce), server sau đó xác thực chữ ký này để 
    # không ai có thể sửa đổi data (Amount, To...)
    
    return jsonify({
        "status": "success",
        "message": f"Transferred {data.get('amount', 0)} to {data.get('to', 'unknown')} securely"
    }), 200

if __name__ == '__main__':
    # Chạy ở port 5002
    app.run(port=5002, debug=True)
