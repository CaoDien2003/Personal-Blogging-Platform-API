from flask import Blueprint, request, jsonify, render_template
from app.auth import AuthService
from app.blog import BlogService

# Define Blueprint
blog_bp = Blueprint('blog', __name__, template_folder="../templates")

# Instantiate Services
auth_service = AuthService()
blog_service = BlogService()

@blog_bp.route('/', methods=['GET'])
@auth_service.token_required()
def get_blogs():
    """
    Description: Get a list of all posts.
    Input: None.
    Output: All blog data.
    """
    return blog_service.get_all_blogs()

@blog_bp.route('/<int:id>', methods=['GET'])
@auth_service.token_required()
def get_blog(id):
    """
    Description: Fetch details of a specific blog by its ID.
    Input:
    - id (int): Blog ID.
    Output: JSON response with the blog details or an error message.
    """
    return blog_service.get_blog(id)

@blog_bp.route('/', methods=['POST'])
@auth_service.token_required(role='admin')
def create_blog(current_user):
    """
    Description: Create a new blog post (Admin only).
    Input: JSON with `title` and `content`.
    Output: JSON response with the blog ID or an error message.
    """
    data = request.get_json()
    if not data.get('title') or not data.get('content'):
        return jsonify({'message': 'Title and content are required'}), 400

    blog_id = blog_service.create_blog(data, current_user)
    if blog_id:
        return jsonify({'message': 'Blog created successfully', 'id': blog_id}), 201
    return jsonify({'message': 'Failed to create blog'}), 500

@blog_bp.route('/<int:id>', methods=['PUT'])
@auth_service.token_required(role='admin')
def update_blog(current_user, id):
    """
    Description: Update an existing blog post (Admin only).
    Input: Blog ID and JSON with updated `title` and `content`.
    Output: JSON response indicating success or failure.
    """
    data = request.get_json()
    response = blog_service.update_blog(id, data, current_user)
    if response['message'] == 'Blog updated successfully':
        return jsonify(response), 200
    return jsonify(response), 500

@blog_bp.route('/<int:id>', methods=['DELETE'])
@auth_service.token_required(role='admin')
def delete_blog(current_user, id):
    """
    Description: Delete a blog post (Admin only).
    Input: Blog ID.
    Output: JSON response indicating success or failure.
    """
    return blog_service.delete_blog(id)
