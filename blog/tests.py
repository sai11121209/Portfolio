from django.test import TestCase
from .models import Posts
from django.contrib.auth.models import User
from faker import Faker
from django.contrib.auth.hashers import make_password
# Create your tests here.

class PostsModelTest(TestCase):
    def test_is_empty(self):
        saved_posts = Posts.objects.all()
        self.assertEqual(saved_posts.count(), 0)

    def setUp(self):
        self.fake_ja = Faker('ja_JP')
        self.fake_en = Faker()

    def setup_is_dummyuser(self, fake, N, M, su):
        dummy_deta = fake.profile()
        users = []
        for i in range(N,M+1):
            users.append(User.objects.create(
                id=i,
                username=dummy_deta['username'],
                first_name=dummy_deta['name'].split()[1],
                last_name=dummy_deta['name'].split()[0],
                email=dummy_deta['mail'],
                is_superuser=su,
                is_staff=False,
                is_active=True,
                date_joined=self.fake_ja.date_time_ad(),
                last_login=self.fake_ja.date_time_ad(),
                password=make_password(self.fake_ja.password(length=10)),
            ))
        return users

    def setup_is_dummyposts(self, fake, N):
        dummy_deta = fake.profile()
        for i in range(1,N+1):
            Posts.objects.create(
                id=i,
                author_id=1,
                title=dummy_deta['company'],
                tags=dummy_deta['name'],
                text=dummy_deta['residence'],
                created_date=fake.date_time_ad(),
                update_date=fake.date_time_ad(),
            )

    def test_is_dummyposts_ja(self):
        self.setup_is_dummyuser(self.fake_ja, 1, 1, False)
        self.setup_is_dummyposts(self.fake_ja, 1)
        saved_posts = Posts.objects.all()
        self.assertEqual(saved_posts.count(), 1)

    def test_is_dummyposts_en(self):
        self.setup_is_dummyuser(self.fake_en, 1, 1, False)
        self.setup_is_dummyposts(self.fake_en, 1)
        saved_posts = Posts.objects.all()
        self.assertEqual(saved_posts.count(), 1)