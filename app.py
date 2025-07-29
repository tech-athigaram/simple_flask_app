from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# 1️⃣ GET /users - List all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# 2️⃣ POST /users - Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    new_user['id'] = len(users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

# 3️⃣ GET /users/<id> - Get user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
