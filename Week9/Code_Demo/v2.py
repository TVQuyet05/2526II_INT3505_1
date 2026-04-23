from flask import Blueprint, request, jsonify

v2_bp = Blueprint('v2', __name__)

@v2_bp.route('/payment', methods=['POST'])
def process_payment():
    data = request.get_json()
    
    if not data or 'amount' not in data or 'currency' not in data:
        return jsonify({"error": "Amount and currency are required"}), 400
        
    amount = data.get('amount')
    currency = data.get('currency')
    
    # Version 2 requires currency specifying
    return jsonify({
        "message": "Payment processed successfully",
        "amount": amount,
        "currency": currency,
        "version": "v2"
    }), 200