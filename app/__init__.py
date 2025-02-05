from flask import Flask
from app.auth.routes import auth_bp
from app.blog.routes import blog_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(blog_bp, url_prefix='/blogs')

    return app
