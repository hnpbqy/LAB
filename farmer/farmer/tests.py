from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client


class FarmerTestCase(TestCase):

    def setUp(self):
        User.objects.create_superuser('testuser',
                                      'testuser@douban.com',
                                      'password')

    def test_home(self):
        client = Client()
        client.login(username='testuser', password='password')
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
