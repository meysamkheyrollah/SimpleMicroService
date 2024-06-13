from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from user.models import User


class UserTokenLoginTest(APITestCase):
    def setUp(self):
        self.url = reverse('user_login')
        self.user = User.objects.create_user(
            phone_number='09901107133',
            national_id='1870316691',
            password='14121372'
        )
    
    def test_user_login_success(self):
        data = {
            "phone_number": '09901107133',
            "password": '14121372'
            }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
    
    def test_user_login_failure(self):
        data = {
            "phone_number": '09901107139',
            "password": '14121372'
            }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn('access', response.data)
        self.assertNotIn('refresh', response.data)

class UserTokenRefreshTest(APITestCase):
    def setUp(self):
        self.login_url = reverse('user_login')
        self.refresh_url = reverse('user_refresh')
        self.user = User.objects.create_user(
            phone_number='09901107123',
            national_id='1870316691',
            password='14121372'
        )
    
        login_data = {
            'phone_number': '09901107123',
            'password': '14121372'
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.refresh_token = response.data['refresh']

    def test_token_refresh_success(self):
        data = {
            'refresh': self.refresh_token
        }
        response = self.client.post(self.refresh_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_token_refresh_failure(self):
        data = {
            'refresh': 'invalidtoken'
        }
        response = self.client.post(self.refresh_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn('access', response.data)

class UserSignUpTest(APITestCase):
    def setUp(self):
        self.url = reverse('user_signup')

    def test_user_signup_success(self):
        data = {
            'phone_number': '09901107123',
            'national_id': '1870316691',
            'password': '14121372'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['phone_number'], '09901107123')
        self.assertEqual(response.data['national_id'], '1870316691')

