import unittest
from unittest.mock import patch, MagicMock
from api_server.database.db_connection import DatabaseConnection

class TestDatabaseConnection(unittest.TestCase):

    @patch('api_server.database.db_connection.mysql.connector.connect')
    def test_successful_connection(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        db = DatabaseConnection()
        connection = db.connect()

        mock_connect.assert_called_once_with(
            host="localhost",
            user="root",
            password="password123",
            database="ecommerce_db"
        )
        self.assertEqual(connection, mock_conn)

    @patch('api_server.database.db_connection.mysql.connector.connect', side_effect=Exception("Connection failed"))
    def test_failed_connection(self, mock_connect):
        db = DatabaseConnection()
        connection = db.connect()

        self.assertIsNone(connection)

    def test_close_connection(self):
        db = DatabaseConnection()
        mock_conn = MagicMock()
        mock_conn.is_connected.return_value = True
        db.connection = mock_conn

        db.close()
        mock_conn.close.assert_called_once()

    def test_close_connection_not_connected(self):
        db = DatabaseConnection()
        mock_conn = MagicMock()
        mock_conn.is_connected.return_value = False
        db.connection = mock_conn

        db.close()
        mock_conn.close.assert_not_called()

if __name__ == "__main__":
    unittest.main()
