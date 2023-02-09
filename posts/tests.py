from django.test import TestCase
from .logics.posts import get_post_with_pk
from .logics.markdown import add_api_url_to_markdown
from .models import Posts
from django.conf import settings


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




