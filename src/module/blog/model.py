from bson.objectid import ObjectId
from src.storage.database import Database

mongo = Database()

class BlogModel:
    @staticmethod
    def create(data):
        """Create a new blog post."""
        return mongo.db.posts.insert_one(data).inserted_id

    @staticmethod
    def get_all(filter=None):
        """Retrieve all blog posts."""
        filter = filter or {}
        return list(mongo.db.posts.find(filter))

    @staticmethod
    def get_by_id(post_id):
        """Retrieve a blog post by ID."""
        return mongo.db.posts.find_one({"_id": ObjectId(post_id)})

    @staticmethod
    def update(post_id, data):
        """Update a blog post by ID."""
        return mongo.db.posts.update_one({"_id": ObjectId(post_id)}, {"$set": data})

    @staticmethod
    def delete(post_id):
        """Delete a blog post by ID."""
        return mongo.db.posts.delete_one({"_id": ObjectId(post_id)})
