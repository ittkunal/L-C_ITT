import unittest
from unittest.mock import patch, MagicMock
from api_server.models.product import Product

class TestProductModel(unittest.TestCase):

    @patch('api_server.models.product.DatabaseConnection')
    def test_save_product(self, MockDBConn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        MockDBConn.return_value.connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        product = Product("Phone", 50000, 1)
        product.save()

        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO products (name, price, category_id) VALUES (%s, %s, %s)",
            ("Phone", 50000, 1)
        )
        mock_conn.commit.assert_called_once()

    @patch('api_server.models.product.DatabaseConnection')
    def test_get_by_category(self, MockDBConn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [{"id": 1, "name": "Phone"}]
        mock_conn.cursor.return_value = mock_cursor
        MockDBConn.return_value.connect.return_value = mock_conn

        products = Product.get_by_category(1)
        self.assertEqual(products, [{"id": 1, "name": "Phone"}])
        mock_cursor.execute.assert_called_once_with(
            "SELECT * FROM products WHERE category_id = %s", (1,)
        )

if __name__ == '__main__':
    unittest.main()
