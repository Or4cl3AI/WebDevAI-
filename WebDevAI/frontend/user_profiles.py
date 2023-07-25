```python
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database connection
DATABASE_URL = "http://localhost:5000/api"

# User schema
USER_SCHEMA = {
    "id": "",
    "username": "",
    "email": "",
    "password": "",
    "profile": {
        "name": "",
        "bio": "",
        "website": ""
    },
    "interactions": []
}

@app.route('/user', methods=['POST'])
def create_user():
    user_data = request.get_json()
    response = requests.post(f"{DATABASE_URL}/users", json=user_data)
    return jsonify(response.json()), response.status_code

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    response = requests.get(f"{DATABASE_URL}/users/{id}")
    return jsonify(response.json()), response.status_code

@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    user_data = request.get_json()
    response = requests.put(f"{DATABASE_URL}/users/{id}", json=user_data)
    return jsonify(response.json()), response.status_code

@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    response = requests.delete(f"{DATABASE_URL}/users/{id}")
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(port=8000)
```