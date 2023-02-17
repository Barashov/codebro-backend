from django.test import TestCase
from rest_framework.test import APIClient
from .logics.posts import get_post_with_pk, get_following_posts
from .logics.markdown import add_api_url_to_markdown
from .models import Posts
from users.models import User
from django.conf import settings


class PostsQueriesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(email='alex@gmail.com')
        cls.user = user
        for _ in range(5):
            post = Posts.objects.create(name='a',
                                        markdown='a',
                                        description='f')
            post.followers.add(user)
        for _ in range(3):
            Posts.objects.create(name='a',
                                 markdown='a',
                                 description='a')

    def test_get_following_posts(self):
        self.assertTrue(len(get_following_posts(self.user)) == 5)
        self.assertFalse(len(get_following_posts(self.user)) == 8)
        self.assertTrue(get_following_posts(66) is None)
        self.assertTrue(get_following_posts(None) is None)


class LogicsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Posts.objects.create(name='python',
                             markdown='# python post',
                             description='python is fast')

    def test_get_none_post_with_pk(self):
        post = get_post_with_pk(44)
        self.assertEqual(post, None)

    def test_get_posts_with_pk(self):
        post = get_post_with_pk(1)
        self.assertEqual(post.name, 'python')

    def test_api_url_to_markdown(self):
        markdown = '[API_URL]'
        self.assertEqual(add_api_url_to_markdown(markdown),
                         settings.API_URL)




