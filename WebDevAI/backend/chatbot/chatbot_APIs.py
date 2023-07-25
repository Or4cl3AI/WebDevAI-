```python
from flask import Flask, request, jsonify
from chatbot import Chatbot

app = Flask(__name__)
chatbot = Chatbot()

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json['user_input']
    response = chatbot.get_response(user_input)
    return jsonify(response)

@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    user_id = request.args.get('user_id')
    recommendations = chatbot.get_recommendations(user_id)
    return jsonify(recommendations)

@app.route('/api/website_content', methods=['GET', 'POST'])
def website_content():
    if request.method == 'POST':
        content = request.json['content']
        chatbot.save_website_content(content)
        return jsonify({'message': 'Content saved successfully.'}), 201
    else:
        content = chatbot.get_website_content()
        return jsonify(content)

if __name__ == '__main__':
    app.run(debug=True)
```