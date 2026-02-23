# Create your tests here.

from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from posts.models import Post

User = get_user_model()

class FollowFeedTests(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='pass')
        self.user2 = User.objects.create_user(username='user2', password='pass')
        self.post2 = Post.objects.create(author=self.user2, title='Hello', content='World')
        self.client.login(username='user1', password='pass')

    def test_follow_user_and_feed(self):
        # user1 follows user2
        url = reverse('follow-user', kwargs={'user_id': self.user2.id})
        self.client.post(url)

        # feed should include user2's post
        feed_url = reverse('feed')
        response = self.client.get(feed_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Hello')

