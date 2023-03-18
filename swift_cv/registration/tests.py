from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import User

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.user_data = {
            'Firstname': 'testuser2',
            'Lastname': 'testuserlastname',
            'Email': 'testuser23@example.com',
            'Password': 'testpass',
            'Retype': 'testpass'
        }
        self.user = User.objects.create_user(username= 'testuser',first_name='testuser',last_name='testuserlastname',email='testuser@example.com',password='testpass')

    def test_signup_view(self):
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_login_view(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'psw': 'testpass'})
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertTrue(response.url, reverse('index'))

    def test_invalid_login_view(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'psw': 'wrongpass'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Username or password is incorrect!!!")
