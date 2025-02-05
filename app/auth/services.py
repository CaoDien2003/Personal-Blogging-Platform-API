import jwt
from flask import current_app, jsonify, request
from functools import wraps
from app.storage.services import DB_Service
from werkzeug.security import check_password_hash, generate_password_hash

class AuthService:
    def __init__(self):
        """
        Description: Initialize the AuthService class.
        Purpose: Set up the connection to the database service.
        """
        self.db_service = DB_Service()

    def create_token(self, user_id, role):
        """
        Description: Create a JWT token for authentication.
        Input:
            - user_id (int): The ID of the authenticated user.
            - role (str): The role of the user (e.g., 'admin', 'user').
        Output:
            - A signed JWT token (string) that contains the user's ID and role.
        Raises:
            - ValueError: If `user_id` or `role` is missing.
        """
        if not user_id or not role:
            raise ValueError("User ID and Role are required to create a token.")
        
        payload = {'user_id': user_id, 'role': role}  # Payload with user data
        secret_key = current_app.config['SECRET_KEY']  # Secret key from app config
        token = jwt.encode(payload, secret_key, algorithm='HS256')  # Encode the token
        return token

    def token_required(self, f=None, role=None):
        """
        Description: Middleware to protect routes with JWT token authentication.
        Input:
            - f (function): The route function to be protected.
            - role (str, optional): The required user role to access the route.
        Output:
            - If valid:
                - Calls the protected function `f` with the current user as an argument.
            - If invalid:
                - Returns a JSON error message with the appropriate status code.
        """
        if f is None:
            return lambda x: self.token_required(x, role=role)

        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')  # Get token from headers
            if not token:
                return jsonify({'message': 'Token is missing'}), 401

            try:
                # Decode the token
                secret_key = current_app.config['SECRET_KEY']  # Secret key for decoding
                data = jwt.decode(token, secret_key, algorithms=['HS256'])
                user_id = data.get('user_id')  # Extract user ID from token payload

                # Fetch user from the database
                query = "SELECT * FROM users WHERE id = %s"
                user = self.db_service.fetch_one(query, (user_id,))
                if not user:
                    return jsonify({'message': 'User not found'}), 401

                # Check if the role matches
                if role and user['role'] != role:
                    return jsonify({'message': 'Unauthorized access'}), 403

                # Pass user info to the protected route
                return f(user, *args, **kwargs)
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token has expired'}), 401
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid token'}), 401

        return decorated

    def login(self):
        """
        Description: Authenticate a user by validating their credentials.
        Input:
            - username (str): The username of the user.
            - password (str): The user's password.
        Output:
            - If valid:
                - JSON response with the JWT token and status code 200.
            - If invalid:
                - JSON response with an error message and status code 401.
        """
        data = request.get_json()  # Get JSON data from the request
        username = data.get('username')
        password = data.get('password')

        # Query to fetch the user from the database
        query = "SELECT * FROM users WHERE username=%s"
        user = self.db_service.fetch_one(query, (username,))

        # Debugging: Print query details
        print(f"Query: {query} | Params: {username}")
        print(f"User fetched: {user}")

        # Check if user exists and validate the password
        if user and check_password_hash(user['password'], password):
            token = self.create_token(user['id'], user['role'])  # Create a JWT token
            return jsonify({'token': token}), 200  # Return token
        else:
            return jsonify({'message': 'Invalid credentials'}), 401  # Error response

    def register(self):
        """
        Description: Register a new user by adding their details to the database.
        Input:
            - username (str): The username of the user.
            - password (str): The user's password.
            - role (str): The role of the user (e.g., 'admin', 'user').
        Output:
            - Success: JSON response indicating successful registration.
            - Failure: JSON response with an error message.
        """
        data = request.get_json()  # Get JSON data from the request
        username = data.get('username')
        password = data.get('password')
        role = data.get('role')

        # Check if the user already exists
        query = "SELECT * FROM users WHERE username=%s"
        user = self.db_service.fetch_one(query, (username,))
        if user:
            return jsonify({'message': 'User already exists'}), 400

        # Hash the password before saving
        hashed_password = generate_password_hash(password)

        # Insert the new user into the database
        query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s) RETURNING id"
        params = (username, hashed_password, role)
        try:
            result = self.db_service.fetch_one(query, params)
            if result:
                return jsonify({'message': 'User registered successfully', 'id': result['id']}), 201
            return jsonify({'message': 'Failed to register user'}), 500
        except Exception as e:
            print(f"Error registering user: {e}")
            return jsonify({'message': 'Internal server error'}), 500