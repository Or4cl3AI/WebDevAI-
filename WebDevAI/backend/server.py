```python
from flask import Flask, request, jsonify
from database import DatabaseConnection
from content_management_system import CMS

app = Flask(__name__)

# Shared dependencies
database_connection = DatabaseConnection()
cms = CMS(database_connection)

@app.route('/')
def home():
    return "Welcome to WebDevAI!"

@app.route('/content', methods=['GET'])
def get_content():
    content = cms.get_all_content()
    return jsonify(content), 200

@app.route('/content', methods=['POST'])
def create_content():
    data = request.get_json()
    content = cms.create_content(data)
    return jsonify(content), 201

@app.route('/content/<content_id>', methods=['PUT'])
def update_content(content_id):
    data = request.get_json()
    content = cms.update_content(content_id, data)
    return jsonify(content), 200

@app.route('/content/<content_id>', methods=['DELETE'])
def delete_content(content_id):
    cms.delete_content(content_id)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
```