```python
import requests
from flask import Flask, request, jsonify
from WebDevAI.backend.database import DatabaseConnection, UserSchema

app = Flask(__name__)

# Shared dependencies
database_connection = DatabaseConnection()
user_schema = UserSchema()

@app.route('/user_interactions', methods=['POST'])
def record_user_interaction():
    """
    Record user interactions with the chatbot and store them in the database.
    """
    user_interaction = request.get_json()
    user_id = user_interaction['user_id']
    interaction = user_interaction['interaction']

    # Validate user interaction
    if not user_schema.validate_interaction(interaction):
        return jsonify({'message': 'Invalid interaction'}), 400

    # Record interaction in the database
    database_connection.record_interaction(user_id, interaction)

    return jsonify({'message': 'Interaction recorded successfully'}), 200

@app.route('/user_interactions/<user_id>', methods=['GET'])
def get_user_interactions(user_id):
    """
    Retrieve a user's interactions with the chatbot from the database.
    """
    interactions = database_connection.get_interactions(user_id)

    if interactions is None:
        return jsonify({'message': 'User not found'}), 404

    return jsonify({'interactions': interactions}), 200

if __name__ == '__main__':
    app.run(debug=True)
```