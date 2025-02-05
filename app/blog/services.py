from flask import jsonify
from app.storage import DB_Service

class BlogService:
    def __init__(self):
        self.db_service = DB_Service()

    def get_all_blogs(self):
        """Fetch all blogs."""
        query = "SELECT * FROM blogs"
        blogs = self.db_service.fetch_all(query)
        if blogs:
            return jsonify([dict(blog) for blog in blogs]), 200
        return jsonify({'message': 'No blogs found'}), 404

    def get_blog(self, blog_id):
        """Fetch a specific blog by ID."""
        query = "SELECT * FROM blogs WHERE id = %s"
        blog = self.db_service.fetch_one(query, (blog_id,))
        if blog:
            return jsonify(dict(blog)), 200
        return jsonify({'message': 'Blog not found'}), 404

    def create_blog(self, data, current_user):
        """Create a new blog post."""
        query = "INSERT INTO blogs (title, author, content) VALUES (%s, %s, %s) RETURNING id"
        params = (data.get('title'), current_user['username'], data.get('content'))
        try:
            result = self.db_service.fetch_one(query, params)
            if result:
                return result['id']
            return None
        except Exception as e:
            print(f"Error creating blog: {e}")
            return None

    def update_blog(self, blog_id, data, current_user):
        """Update an existing blog post."""
        query = "UPDATE blogs SET title = %s, content = %s WHERE id = %s"
        params = (data.get('title'), data.get('content'), blog_id)
        try:
            result = self.db_service.execute_query(query, params)
            if result:
                return {'message': 'Blog updated successfully'}
        except Exception as e:
            print(f"Error updating blog ID {blog_id}: {e}")
        return {'message': 'Failed to update blog'}

    def delete_blog(self, blog_id):
        """Delete a blog post."""
        query = "DELETE FROM blogs WHERE id = %s"
        try:
            result = self.db_service.execute_query(query, (blog_id,))
            if result:
                return jsonify({'message': 'Blog deleted successfully'}), 200
        except Exception as e:
            print(f"Error deleting blog ID {blog_id}: {e}")
        return jsonify({'message': 'Failed to delete blog'}), 500
