import configparser

class DBPropertyUtil:

    @staticmethod
    def get_connection_string(property_file: str) -> str:
        config = configparser.ConfigParser()
        config.read(property_file)

        try:
            server = config.get('database', 'server')
            database = config.get('database', 'database')
            username = config.get('database', 'username')
            password = config.get('database', 'password')
            driver = config.get('database', 'driver')

            return f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

        except Exception as e:
            from exception.database_connection_exception import DatabaseConnectionException
            raise DatabaseConnectionException(f"Error reading DB properties: {e}")
