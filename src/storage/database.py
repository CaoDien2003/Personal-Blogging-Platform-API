from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from src.config import Config

class Database:
    def __init__(self):

        self.client = MongoClient(Config.MONGO_URI, server_api=ServerApi('1'))
        self.db = self.client["blog"]

    def test_connection(self):
        """Ping MongoDB to check the connection."""
        try:
            self.client.admin.command('ping')
            print("Successfully connected to MongoDB!")
        except Exception as e:
            print(f"Connection error: {e}")
