from django.test import TestCase

from Online_shop.accounts.models import ShopUser
from Online_shop.main_app.models import Plant


class URLTestsPlants(TestCase):

    def test_plantspage(self):
        response = self.client.get('/plants/')
        self.assertEqual(response.status_code, 200)

    def test_create_plantspage(self):
        response = self.client.get('/plants/create/')
        self.assertEqual(response.status_code, 302)

    def test_edit_plantspage(self):
        ShopUser.objects.create(username='django1', password='Valkyrie123', is_staff=1, is_superuser=1)
        Plant.objects.create(name='Kala', quantity='5', type='Winter plant'
                             , description='Beautiful Necklace', price='5.23', user_key_id=3)
        response = self.client.get('/plants/edit/1')
        self.assertEqual(response.status_code, 302)

    def test_details_plantspage(self):
        response = self.client.get('/plants/details/1')
        self.assertEqual(response.status_code, 404)

    def test_delete_plantspage(self):
        delete_response = self.client.get('/plants/delete/1')
        self.assertEqual(delete_response.status_code, 404)