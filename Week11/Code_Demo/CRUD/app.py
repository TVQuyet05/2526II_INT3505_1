from flask import Flask, request, jsonify

app = Flask(__name__)

# Giả lập Database trong RAM
users = {}
current_id = 1

# 1. CREATE: POST /users
@app.route('/users', methods=['POST'])
def create_user():
    global current_id
    data = request.json
    user = {'id': current_id, 'name': data.get('name'), 'email': data.get('email')}
    users[current_id] = user
    current_id += 1
    return jsonify(user), 201

# 2. READ (All): GET /users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

# 3. READ (One): GET /users/<id>
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

# 4. UPDATE: PUT /users/<id>
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.json
        users[user_id].update({
            'name': data.get('name', users[user_id]['name']),
            'email': data.get('email', users[user_id]['email'])
        })
        return jsonify(users[user_id]), 200
    return jsonify({'error': 'User not found'}), 404

# 5. DELETE: DELETE /users/<id>
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return '', 204 # No Content
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    print("Starting CRUD API on port 5002...")
    app.run(port=5002)