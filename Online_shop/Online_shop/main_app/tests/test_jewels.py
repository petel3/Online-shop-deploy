from django.test import TestCase

from Online_shop.accounts.models import ShopUser
from Online_shop.main_app.models import Jewelry


class URLTestsJewelry(TestCase):

    def test_jewelrypage(self):
        response = self.client.get('/jewelry/')
        self.assertEqual(response.status_code, 200)

    def test_create_jewelrypage(self):
        response = self.client.get('/jewelry/create/')
        self.assertEqual(response.status_code, 302)

    def test_edit_jewelrypage(self):
        ShopUser.objects.create(username='django1', password='Valkyrie123', is_staff=1, is_superuser=1)
        Jewelry.objects.create(name='Necklace', quantity='3', materials='Silver'
                               , description='Beautiful Necklace', price='5.23', user_key_id=2)
        response = self.client.get('/jewelry/edit/1')
        self.assertEqual(response.status_code, 200)

    def test_details_jewelrypage(self):
        response = self.client.get('/jewelry/details/1')
        self.assertEqual(response.status_code, 302)

    def test_delete_jewelrypage(self):
        response = self.client.get('/jewelry/details/1')
        self.assertEqual(response.status_code, 302)
        delete_response = self.client.get('/jewelry/delete/1')
        self.assertEqual(delete_response.status_code, 404)