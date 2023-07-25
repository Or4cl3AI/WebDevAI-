```python
import os
from flask import Flask, render_template, request
from WebDevAI.backend.content_management_system import CMS

app = Flask(__name__)
cms = CMS()

@app.route('/create_page', methods=['POST'])
def create_page():
    page_data = request.get_json()
    page_name = page_data['page_name']
    page_content = page_data['page_content']
    cms.create_page(page_name, page_content)
    return {"message": "Page created successfully"}, 200

@app.route('/edit_page', methods=['PUT'])
def edit_page():
    page_data = request.get_json()
    page_name = page_data['page_name']
    page_content = page_data['page_content']
    cms.edit_page(page_name, page_content)
    return {"message": "Page edited successfully"}, 200

@app.route('/delete_page', methods=['DELETE'])
def delete_page():
    page_name = request.args.get('page_name')
    cms.delete_page(page_name)
    return {"message": "Page deleted successfully"}, 200

@app.route('/<page_name>', methods=['GET'])
def serve_page(page_name):
    page_content = cms.get_page_content(page_name)
    if page_content:
        return render_template('page.html', content=page_content)
    else:
        return {"message": "Page not found"}, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5000))
```