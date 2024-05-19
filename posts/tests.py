from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='testuser', password='123')
        cls.post = Post.objects.create(title='Test Post', content='Test content', author=cls.user)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Test Post')
        self.assertEqual(f'{self.post.author}', 'testuser')

    def test_user_content(self):
        self.assertEqual(f'{self.user.username}', 'testuser')
        self.assertEqual(f'{self.user.email}', '')
