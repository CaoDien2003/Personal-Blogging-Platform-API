from flask import blueprints,request,render_template
import jwt

# Function to create JWT token
def create_token(user_id):
    payload = {'user_id': user_id}
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token


# Middleware: Verify JWT Token
def token_required(f=None, role=None):
    if f is None:
        return lambda x: token_required(x, role=role)

    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            user_id = data['user_id']

            cursor.execute('SELECT * FROM users WHERE id=%s', (user_id,))
            user = cursor.fetchone()

            if not user:
                return jsonify({'message': 'User not found'}), 401

            if role and user['role'] != role:
                return jsonify({'message': 'Unauthorized access'}), 403
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

        return f(*args, **kwargs)

    return decorated


# Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    cursor.execute('SELECT * FROM users WHERE username=%s', (username,))
    user = cursor.fetchone()

    if user and check_password_hash(user['password'], password):
        token = create_token(user['id'])
        return jsonify({'token': token})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401