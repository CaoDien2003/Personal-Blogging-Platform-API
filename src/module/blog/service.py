from src.module.blog.model import BlogModel

class BlogService:
    @staticmethod
    def create_post(data):
        """Validate and create a blog post."""
        if not data.get("title") or not data.get("content"):
            return {"error": "Title and content are required."}, 400
        post_id = BlogModel.create(data)
        return {"id": str(post_id)}, 201

    @staticmethod
    def get_posts(term=None):
        """Retrieve all or filtered blog posts."""
        filter = {"$or": [
            {"title": {"$regex": term, "$options": "i"}},
            {"content": {"$regex": term, "$options": "i"}},
            {"category": {"$regex": term, "$options": "i"}}
        ]} if term else {}
        posts = BlogModel.get_all(filter)
        for post in posts:
            post["_id"] = str(post["_id"])  # Convert ObjectId to string
        return posts, 200

    @staticmethod
    def get_post(post_id):
        """Retrieve a single blog post by ID."""
        post = BlogModel.get_by_id(post_id)
        if not post:
            return {"error": "Post not found."}, 404
        post["_id"] = str(post["_id"])
        return post, 200

    @staticmethod
    def update_post(post_id, data):
        """Update a blog post."""
        result = BlogModel.update(post_id, data)
        if result.matched_count == 0:
            return {"error": "Post not found."}, 404
        return {"message": "Post updated successfully."}, 200

    @staticmethod
    def delete_post(post_id):
        """Delete a blog post."""
        result = BlogModel.delete(post_id)
        if result.deleted_count == 0:
            return {"error": "Post not found."}, 404
        return {"message": "Post deleted successfully."}, 204
