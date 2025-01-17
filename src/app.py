from flask import Flask
from flask_restful import Api
from config import Config
from module.blog.api import BlogAPI
from storage.database import Database

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize MongoDB
mongo = Database()
mongo.test_connection()

# Register API
api = Api(app)
api.add_resource(BlogAPI, "/posts", "/posts/<string:post_id>")

if __name__ == "__main__":
    app.run(debug=True)
