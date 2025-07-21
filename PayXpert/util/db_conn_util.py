import pyodbc
from exception.database_connection_exception import DatabaseConnectionException

class DBConnUtil:

    @staticmethod
    def get_connection(conn_string: str):
        try:
            connection = pyodbc.connect(conn_string)
            return connection
        except Exception as e:
            raise DatabaseConnectionException(f"Failed to connect to the database: {e}")
