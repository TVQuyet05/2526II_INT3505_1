from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook_receiver():
    if request.is_json:
        data = request.get_json()
        print(f"Received webhook event: {data.get('event')}")
        print(f"Payload: {data.get('payload')}")
        return jsonify({"status": "success", "message": "Webhook received"}), 200
    else:
        return jsonify({"status": "error", "message": "Request must be JSON"}), 400

if __name__ == '__main__':
    print("Starting Webhook Receiver on port 5001...")
    app.run(port=5001)
