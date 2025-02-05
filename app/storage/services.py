import psycopg2
import psycopg2.extras
from app.storage.config import DB_CONFIG

class DB_Service:
    def __init__(self):
        """
        Description: Initialize the database service and establish a connection to the PostgreSQL database.
        Purpose: Set up a reusable database connection using parameters from `DB_CONFIG`.
        Input:
            - None.
        Output:
            - A database connection object and cursor.
        Exceptions:
            - If a connection error occurs, the connection is set to `None` and the error is printed.
        """
        try:
            self.connection = psycopg2.connect(
                dbname=DB_CONFIG['DB_NAME'],
                user=DB_CONFIG['DB_USER'],
                password=DB_CONFIG['DB_PASSWORD'],
                host=DB_CONFIG['DB_HOST'],
                port=DB_CONFIG['DB_PORT']
            )
            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        except Exception as e:
            print(f"Database connection error: {e}")
            self.connection = None

    def execute_query(self, query, params=None):
        """
        Description: Execute an SQL query (INSERT, UPDATE, DELETE) on the database.
        Input:
            - query (string): The SQL query to be executed.
            - params (tuple, optional): The parameters for the SQL query.
        Output:
            - Success: A dictionary with the message `Query executed successfully`.
            - Failure: A dictionary with the message `Query execution failed` and the error details.
        Exceptions:
            - Rolls back the transaction if an error occurs.
        """
        if not self.connection:
            return {'message': 'No database connection'}
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return {'message': 'Query executed successfully'}
        except Exception as e:
            self.connection.rollback()
            return {'message': 'Query execution failed', 'error': str(e)}

    def fetch_one(self, query, params=None):
        """
        Description: Fetch a single record from the database.
        Input:
            - query (string): The SQL query to be executed.
            - params (tuple, optional): The parameters for the SQL query.
        Output:
            - Success: A dictionary representing a single record from the database.
            - Failure: None if the query fails or no record is found.
        """
        if not self.connection:
            return None
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error fetching one record: {e}")
            return None

    def fetch_all(self, query, params=None):
        """
        Description: Fetch all records from the database.
        Input:
            - query (string): The SQL query to be executed.
            - params (tuple, optional): The parameters for the SQL query.
        Output:
            - Success: A list of dictionaries representing all matching records.
            - Failure: None if the query fails or no records are found.
        """
        if not self.connection:
            return None
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching all records: {e}")
            return None

    def close_connection(self):
        """
        Description: Close the database connection and the cursor.
        Input:
            - None.
        Output:
            - None.
        """
        if self.connection:
            self.cursor.close()
            self.connection.close()