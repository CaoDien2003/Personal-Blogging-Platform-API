from flask_restful import Resource
from flask import request
from src.module.blog.service import BlogService

class BlogAPI(Resource):
    def get(self, post_id=None):
        """Retrieve blog posts or a specific post."""
        term = request.args.get("term")
        if post_id:
            return BlogService.get_post(post_id)
        return BlogService.get_posts(term)

    def post(self):
        """Create a new blog post."""
        data = request.get_json()
        return BlogService.create_post(data)

    def put(self, post_id):
        """Update a blog post."""
        data = request.get_json()
        return BlogService.update_post(post_id, data)

    def delete(self, post_id):
        """Delete a blog post."""
        return BlogService.delete_post(post_id)
