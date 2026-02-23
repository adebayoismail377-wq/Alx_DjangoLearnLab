# Create your tests here.
from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Post


class PostTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='pass')
        self.client.login(username='test', password='pass')

    def test_create_post(self):
        response = self.client.post('/api/posts/', {
            'title': 'Test Post',
            'content': 'Test content'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)