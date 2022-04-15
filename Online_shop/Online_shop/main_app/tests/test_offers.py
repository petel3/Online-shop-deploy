from django.test import TestCase

class URLTestsOffers(TestCase):

    def test_offerspage(self):
        response = self.client.get('/quotations/')
        self.assertEqual(response.status_code, 200)