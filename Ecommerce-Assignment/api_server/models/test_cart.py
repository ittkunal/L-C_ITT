import unittest
from unittest.mock import patch, MagicMock
from api_server.models.cart import Cart

class TestCartModel(unittest.TestCase):

    @patch('api_server.models.cart.DatabaseConnection')
    def test_save_cart(self, MockDBConn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.lastrowid = 123
        mock_conn.cursor.return_value = mock_cursor
        MockDBConn.return_value.connect.return_value = mock_conn

        cart = Cart(1, 2, 3)
        cart.save()

        self.assertEqual(cart.id, 123)
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO carts (user_id, product_id, quantity) VALUES (%s, %s, %s)",
            (1, 2, 3)
        )

    @patch('api_server.models.cart.DatabaseConnection')
    def test_get_by_user(self, MockDBConn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [{"user_id": 1, "product_id": 2}]
        mock_conn.cursor.return_value = mock_cursor
        MockDBConn.return_value.connect.return_value = mock_conn

        result = Cart.get_by_user(1)
        self.assertEqual(result, [{"user_id": 1, "product_id": 2}])

if __name__ == '__main__':
    unittest.main()
