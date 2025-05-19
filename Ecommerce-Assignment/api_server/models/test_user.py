import unittest
from unittest.mock import patch, MagicMock
from api_server.models.user import User

class TestUserModel(unittest.TestCase):

    @patch('api_server.models.user.DatabaseConnection')
    def test_user_save_success(self, MockDBConn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        MockDBConn.return_value.connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        user = User("testuser", "testpass")
        user.save()

        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            ("testuser", "testpass")
        )
        mock_conn.commit.assert_called_once()

    @patch('api_server.models.user.DatabaseConnection')
    def test_user_save_failure(self, MockDBConn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.execute.side_effect = Exception("Insert failed")
        mock_conn.cursor.return_value = mock_cursor
        MockDBConn.return_value.connect.return_value = mock_conn

        user = User("failuser", "failpass")
        user.save()

        mock_conn.rollback.assert_called_once()

if __name__ == '__main__':
    unittest.main()
