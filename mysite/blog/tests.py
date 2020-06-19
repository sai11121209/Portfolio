from django.test import TestCase
from .models import Posts
from faker import Faker
# Create your tests here.

class PostsModelTest(TestCase):
    def test_is_empty(self):
        saved_posts = Posts.objects.all()
        self.assertEqual(saved_posts.count(), 0)