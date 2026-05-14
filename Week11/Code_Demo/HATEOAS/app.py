from flask import Flask, jsonify, request

app = Flask(__name__)

# Giả lập Database với các trạng thái khác nhau
orders = {
    1: {"id": 1, "item": "Laptop", "status": "pending", "price": 1200},
    2: {"id": 2, "item": "Mouse", "status": "paid", "price": 25},
    3: {"id": 3, "item": "Desk", "status": "shipped", "price": 150}
}

def generate_links(order_id, status):
    """
    Tạo mảng links (HATEOAS) phụ thuộc vào trạng thái (state) hiện tại của đối tượng.
    """
    base_url = f"http://localhost:5004/orders/{order_id}"
    links = [
        {"rel": "self", "href": base_url, "method": "GET"} # Luôn có link tham chiếu đến chính nó
    ]
    
    # State Machine: Nếu pending -> Có thể pay (thanh toán) hoặc cancel (hủy)
    if status == "pending":
        links.append({"rel": "pay", "href": f"{base_url}/pay", "method": "POST"})
        links.append({"rel": "cancel", "href": f"{base_url}/cancel", "method": "POST"})
        
    # State Machine: Nếu paid -> Có thể ship (giao hàng)
    elif status == "paid":
        links.append({"rel": "ship", "href": f"{base_url}/ship", "method": "POST"})
        links.append({"rel": "refund", "href": f"{base_url}/refund", "method": "POST"})
        
    return links

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
        
    response = order.copy()
    # Nhúng thông tin HATEOAS vào response
    response["_links"] = generate_links(order_id, order["status"])
    return jsonify(response), 200

@app.route('/orders/<int:order_id>/pay', methods=['POST'])
def pay_order(order_id):
    order = orders.get(order_id)
    if order and order["status"] == "pending":
        order["status"] = "paid"
        return get_order(order_id) # Trả về state mới kèm các link mới (ship, refund)
    return jsonify({"error": "Cannot pay this order. Invalid state."}), 400

if __name__ == '__main__':
    print("Starting HATEOAS API on port 5004...")
    print("Try: GET http://localhost:5004/orders/1")
    app.run(port=5004)