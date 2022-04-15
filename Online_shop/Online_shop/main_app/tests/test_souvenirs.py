from django.test import TestCase

from Online_shop.accounts.models import ShopUser
from Online_shop.main_app.models import Souvenir


class URLTestsSouvenirs(TestCase):

    def test_souvenirspage(self):
        response = self.client.get('/souvenirs/')
        self.assertEqual(response.status_code, 200)

    def test_create_souvenirspage(self):
        response = self.client.get('/souvenirs/create/')
        self.assertEqual(response.status_code, 302)

    def test_edit_souvenirspage(self):
        ShopUser.objects.create(username='django1', password='Valkyrie123', is_staff=1, is_superuser=1)
        Souvenir.objects.create(name='Glass', quantity='2', type='Normal'
                                , description='Beautiful Glass', price='35.23', user_key_id=4)
        response = self.client.get('/souvenirs/edit/1')
        self.assertEqual(response.status_code, 200)

    def test_details_souvenirspage(self):
        response = self.client.get('/souvenirs/details/1')
        self.assertEqual(response.status_code, 302)

    def test_delete_souvenirspage(self):
        delete_response = self.client.get('/souvenirs/delete/1')
        self.assertEqual(delete_response.status_code, 404)