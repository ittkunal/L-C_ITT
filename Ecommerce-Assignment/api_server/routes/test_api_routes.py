import unittest
from unittest.mock import patch, MagicMock
from api_server.routes import api_routes

class TestApiRoutes(unittest.TestCase):

    def setUp(self):
        self.app = api_routes.app.test_client()
        self.app.testing = True

    @patch('api_server.routes.api_routes.auth_service.signup')
    @patch('api_server.routes.api_routes.get_db_connection')
    def test_signup_success(self, mock_get_db_conn, mock_signup):
        
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchone.side_effect = [None, {'id': 1}]  
        mock_conn.cursor.return_value = mock_cursor
        mock_get_db_conn.return_value = mock_conn
        mock_signup.return_value = 1

        response = self.app.post('/signup', json={'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('user_id', response.get_json())

    @patch('api_server.routes.api_routes.get_db_connection')
    def test_signup_user_exists(self, mock_get_db_conn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {'id': 1}  
        mock_conn.cursor.return_value = mock_cursor
        mock_get_db_conn.return_value = mock_conn

        response = self.app.post('/signup', json={'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    @patch('api_server.routes.api_routes.auth_service.login')
    def test_login_success(self, mock_login):
        mock_login.return_value = 1
        response = self.app.post('/login', json={'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'user_id': 1})

    @patch('api_server.routes.api_routes.auth_service.login')
    def test_login_failure(self, mock_login):
        mock_login.return_value = None
        response = self.app.post('/login', json={'username': 'wrong', 'password': 'wrong'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json(), {'error': 'Login failed'})

    @patch('api_server.routes.api_routes.category_service.get_all_categories')
    def test_get_categories(self, mock_get_categories):
        mock_get_categories.return_value = [{'id': 1, 'name': 'Books'}]
        response = self.app.get('/categories')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [{'id': 1, 'name': 'Books'}])

    @patch('api_server.routes.api_routes.product_service.get_products_by_category')
    def test_get_products_by_category(self, mock_get_products):
        mock_get_products.return_value = [{'id': 10, 'name': 'Laptop'}]
        response = self.app.get('/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [{'id': 10, 'name': 'Laptop'}])

    @patch('api_server.routes.api_routes.cart_service.add_to_cart')
    def test_add_to_cart(self, mock_add_to_cart):
        response = self.app.post('/cart/add', json={'user_id': 1, 'product_id': 2, 'quantity': 1})
        mock_add_to_cart.assert_called_once_with(1, 2, 1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Added to cart'})

    @patch('api_server.routes.api_routes.order_service.create_order')
    def test_buy_cart(self, mock_create_order):
        mock_create_order.return_value = 100
        response = self.app.post('/cart/buy', json={'user_id': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'order_id': 100})

    @patch('api_server.routes.api_routes.order_service.get_order_history')
    def test_get_order_history(self, mock_order_history):
        mock_order_history.return_value = [{'id': 1, 'total_amount': 123.45}]
        response = self.app.get('/orders/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [{'id': 1, 'total_amount': 123.45}])

    def test_test_endpoint(self):
        response = self.app.get('/test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Server is alive'})

if __name__ == '__main__':
    unittest.main()
