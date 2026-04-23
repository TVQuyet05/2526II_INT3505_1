from flask import Blueprint, request, jsonify

v1_bp = Blueprint('v1', __name__)

@v1_bp.route('/payment', methods=['POST'])
def process_payment():
    data = request.get_json()
    
    if not data or 'amount' not in data:
        return jsonify({"error": "Amount is required"}), 400
        
    amount = data.get('amount')
    
    # Version 1 defaults to VND
    response = jsonify({
        "message": "Payment processed successfully (DEPRECATED)",
        "amount": amount,
        "currency": "VND",
        "version": "v1"
    })
    
    # Adding Deprecation HTTP Headers
    response.headers['Deprecation'] = 'true'  # Đánh dấu API đã deprecated
    response.headers['Sunset'] = 'Thu, 31 Dec 2026 23:59:59 GMT' # Ngày khai tử chính thức
    response.headers['Link'] = '<http://localhost:5000/api/v2/payment>; rel="alternate"' # Link chuyển hướng sang v2
    
    return response, 200