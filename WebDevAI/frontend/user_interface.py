```python
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    response = requests.post('http://localhost:5000/api/chat', json={'message': user_message})
    return response.json()

if __name__ == '__main__':
    app.run(port=8000)
```

This is a simple Flask application for the user interface. It has two routes, the home route which renders the index.html file, and the chat route which sends the user's message to the chatbot API and returns the response. The chat route uses a POST request to send the user's message to the chatbot API. The chatbot API is assumed to be running on localhost port 5000. The user's message is sent as a JSON object with the key 'message'. The response from the chatbot API is returned as a JSON object.