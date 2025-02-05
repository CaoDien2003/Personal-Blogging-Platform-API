import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'postgresql://postgres:caodien1403@localhost:5432/blog_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
