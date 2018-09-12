from unittest import TestCase
import json
from app import create_app


class TestOrders(TestCase):

    def SetUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_create_order(self):
        data = {
            "name":"maiza",
            "price":20,
            "description":"sweet ugali"
        }

        resp = self.client.post(
            "/api/v1/orders",
            data = json.dumps(data),
            headers = {"content-type":"application/json"}
        )

        self.assertEqual(resp.status_code,201)
        self.assertEqual(json.loads(resp.data)['message'],"status approved")

        def test_get_order_by_id(self):
            resp = self.client.get(
                "api/v1/orders/1",
                headers = {"content-type":"application/json"}
            )

            self.assertEqual(resp.status_code,200)

        def test_update_order_status(self):
            resp = self.client.put(
                "api/v1/orders/1",
                headers = {"content-type":"application/json"}
            )

            self.assertEqual(resp.status_code,200)
            self.assertEqual(json.loads(resp.data)['message'],"status approved")

            

        