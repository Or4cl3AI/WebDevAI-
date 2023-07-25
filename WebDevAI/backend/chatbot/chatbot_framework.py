```python
import os
from flask import Flask, request
from chatbot import Chatbot

app = Flask(__name__)
chatbot_instance = Chatbot()

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = chatbot_instance.get_response(user_input)
    return {'message': response}

@app.route('/api/chat/train', methods=['POST'])
def train():
    training_data = request.json['data']
    chatbot_instance.train(training_data)
    return {'message': 'Chatbot trained successfully'}

@app.route('/api/chat/save', methods=['POST'])
def save():
    chatbot_instance.save_model()
    return {'message': 'Chatbot model saved successfully'}

@app.route('/api/chat/load', methods=['POST'])
def load():
    chatbot_instance.load_model()
    return {'message': 'Chatbot model loaded successfully'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```