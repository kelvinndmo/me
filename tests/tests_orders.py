import unittest
import json
from app import create_app


class TestOrders(unittest.TestCase):
    '''set up for testing'''
    
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_create_order(self):
        data = {
            "name": "eggcurry",
            "price": 20,
            "description": "sweet eggs"
        }

        res = self.client.post(
            "/api/v1/orders",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )

        self.assertEqual(res.status_code, 201)
        self.assertEqual(json.loads(res.data)['message'], "Food order created")

    def test_get_all_orders(self):

        res = self.client.get(
            "/api/v1/orders",
            headers={"content-type": "application/json"}
        )

        self.assertEqual(res.status_code, 200)


    def test_order_by_id(self):
        res = self.client.get(
            "/api/v1/orders/1",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    
    def test_update_order_status(self):
        res = self.client.put(
            "api/v1/orders/1",
            headers={"content-type": "application/json"}
        )
        print(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.loads(res.data)[
                         'message'], "status approved")

    
    


    def test_non_order_by_id(self):
        res = self.client.get(
            "/api/v1/orders/111",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 404)
        self.assertEqual(json.loads(res.data)[
                         'message'], "Order not found")


    def test_non_order_delete(self):
        res = self.client.delete(
            "api/v1/orders/11",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 404)
        self.assertEqual(json.loads(res.data)[
                         'message'], "Order not found")