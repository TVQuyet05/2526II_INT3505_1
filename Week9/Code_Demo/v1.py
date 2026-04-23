from flask import Blueprint, request, jsonify

v1_bp = Blueprint('v1', __name__)

@v1_bp.route('/payment', methods=['POST'])
def process_payment():
    data = request.get_json()
    
    if not data or 'amount' not in data:
        return jsonify({"error": "Amount is required"}), 400
        
    amount = data.get('amount')
    
    # Version 1 defaults to VND
    return jsonify({
        "message": "Payment processed successfully",
        "amount": amount,
        "currency": "VND",
        "version": "v1"
    }), 200