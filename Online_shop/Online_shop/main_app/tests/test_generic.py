from django.test import TestCase


class URLTestsGeneric(TestCase):

    def test_indexpage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

