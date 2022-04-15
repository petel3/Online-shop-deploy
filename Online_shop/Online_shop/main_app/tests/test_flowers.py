from django.test import TestCase

from Online_shop.accounts.models import ShopUser
from Online_shop.main_app.models import Flower


class URLTestsFlowers(TestCase):

    def test_flowerspage(self):
        response = self.client.get('/flowers/')
        self.assertEqual(response.status_code, 200)

    def test_create_flowerspage(self):
        response = self.client.get('/flowers/create/')
        self.assertEqual(response.status_code, 302)

    def test_edit_flowerspage(self):
        ShopUser.objects.create(username='django1', password='Valkyrie123', is_staff=1, is_superuser=1)
        Flower.objects.create(name='Rose', quantity='3', type='Basket'
                              , description='Beautiful rose', price='15.23', user_key_id=1)

        response = self.client.get('/flowers/edit/1')
        self.assertEqual(response.status_code, 200)

    def test_details_flowerspage(self):
        response = self.client.get('/flowers/details/1')
        self.assertEqual(response.status_code, 302)

    def test_delete_flowerspage(self):
        response = self.client.get('/flowers/details/1')
        self.assertEqual(response.status_code, 302)
        delete_response = self.client.get('/flowers/delete/1')
        self.assertEqual(delete_response.status_code, 404)