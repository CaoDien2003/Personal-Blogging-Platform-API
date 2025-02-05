from flask import Blueprint, request, jsonify
from app.auth.services import AuthService
from app.storage import DB_Service

# Define the Blueprint for authentication
auth_bp = Blueprint('auth', __name__)

# Instantiate AuthService and DB_Service
auth_service = AuthService()
db_service = DB_Service()

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Description: Authenticate a user and return a JWT token upon successful login.
    Input:
        - username (string): The username of the user.
        - password (string): The password of the user.
    Output:
        - Success: JSON response with a JWT token and status code 200.
        - Failure: JSON response with an error message and status code 401.
    """
    return auth_service.login()

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Description: Register a new user by adding their details to the database.
    Input:
        - username (string): The username of the user.
        - password (string): The password of the user.
        - role (string): The role of the user (e.g., 'admin', 'user').
    Output:
        - Success: JSON response indicating successful registration.
        - Failure: JSON response with an error message.
    """
    return auth_service.register()
