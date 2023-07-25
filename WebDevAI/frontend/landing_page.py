```python
import os
from flask import Flask, render_template, request
from WebDevAI.backend.content_management_system import CMS

app = Flask(__name__)
cms = CMS()

@app.route('/create_landing_page', methods=['GET', 'POST'])
def create_landing_page():
    if request.method == 'POST':
        page_content = request.form['page_content']
        page_title = request.form['page_title']
        page_id = cms.create_page(page_title, page_content)
        return render_template('landing_page.html', page_content=page_content, page_title=page_title)
    return render_template('create_landing_page.html')

@app.route('/edit_landing_page/<page_id>', methods=['GET', 'POST'])
def edit_landing_page(page_id):
    if request.method == 'POST':
        page_content = request.form['page_content']
        page_title = request.form['page_title']
        cms.edit_page(page_id, page_title, page_content)
        return render_template('landing_page.html', page_content=page_content, page_title=page_title)
    page = cms.get_page(page_id)
    return render_template('edit_landing_page.html', page=page)

@app.route('/landing_page/<page_id>')
def view_landing_page(page_id):
    page = cms.get_page(page_id)
    return render_template('landing_page.html', page_content=page['content'], page_title=page['title'])

if __name__ == '__main__':
    app.run(debug=True)
```