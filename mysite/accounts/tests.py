from django.test import TestCase
from django.contrib.auth.models import User
from faker import Faker
from django.contrib.auth.hashers import make_password
# Create your tests here.
class UserModelTest(TestCase):
    def test_is_empty(self):
        saved_posts = User.objects.all()
        self.assertEqual(saved_posts.count(), 0)

    def test_is_dummydata_ja(self):
        fake = Faker('ja_JP')
        dummy_deta = fake.profile()
        User.objects.create(
            username=dummy_deta['username'],
            first_name=dummy_deta['name'].split()[1],
            last_name=dummy_deta['name'].split()[0],
            email=dummy_deta['mail'],
            is_superuser=0,
            is_staff=0,
            is_active=1,
            date_joined=fake.date_time_ad(),
            last_login=fake.date_time_ad(),
            password=make_password(fake.password(length=10)),
            id=1,
        )
        saved_user = User.objects.all()
        self.assertEqual(saved_user.count(), 1)
    def test_is_dummydata_en(self):
        fake = Faker()
        dummy_deta = fake.profile()
        User.objects.create(
            username=dummy_deta['username'],
            first_name=dummy_deta['name'].split()[1],
            last_name=dummy_deta['name'].split()[0],
            email=dummy_deta['mail'],
            is_superuser=0,
            is_staff=0,
            is_active=1,
            date_joined=fake.date_time_ad(),
            last_login=fake.date_time_ad(),
            password=make_password(fake.password(length=10)),
            id=1,
        )
        saved_user = User.objects.all()
        self.assertEqual(saved_user.count(), 1)