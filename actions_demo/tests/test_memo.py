from django.test import TestCase

MEMO_URL = "/demo"

class MemoTestCase(TestCase):

    def setUp(self):
        pass

    def create_memo_success(self):
        reqeust_body = {"title":"Test Title", "user" : "Test user"}
        response = self.client.post(MEMO_URL, data=reqeust_body)
        result = {
            "message" : "success"
        }
        self.assertEqual(response.json(), result)