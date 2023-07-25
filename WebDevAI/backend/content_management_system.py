```python
import pymongo
from bson.objectid import ObjectId

class ContentManagementSystem:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.content_collection = self.db_connection['content']

    def create_content(self, content_data):
        content_id = self.content_collection.insert_one(content_data).inserted_id
        return str(content_id)

    def get_content(self, content_id):
        content_data = self.content_collection.find_one({'_id': ObjectId(content_id)})
        return content_data

    def update_content(self, content_id, updated_content_data):
        self.content_collection.update_one({'_id': ObjectId(content_id)}, {'$set': updated_content_data})

    def delete_content(self, content_id):
        self.content_collection.delete_one({'_id': ObjectId(content_id)})

    def list_all_content(self):
        all_content = self.content_collection.find()
        return [content for content in all_content]

if __name__ == "__main__":
    # Establish a connection to the database
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["WebDevAI"]

    # Create an instance of the CMS
    cms = ContentManagementSystem(db)

    # Example usage
    new_content = {
        "title": "My First Blog Post",
        "body": "This is the body of my first blog post.",
        "author": "John Doe",
        "date_published": "2021-01-01"
    }

    content_id = cms.create_content(new_content)
    print(f"New content created with ID: {content_id}")

    content_data = cms.get_content(content_id)
    print(f"Retrieved content data: {content_data}")

    updated_content = {
        "title": "My Updated Blog Post"
    }

    cms.update_content(content_id, updated_content)
    print(f"Content with ID {content_id} updated")

    cms.delete_content(content_id)
    print(f"Content with ID {content_id} deleted")
```