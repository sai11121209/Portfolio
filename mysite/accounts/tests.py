from django.test import TestCase
from django.contrib.auth.models import User
from faker import Faker
from django.contrib.auth.hashers import make_password

# Create your tests here.
class UserModelTest(TestCase):

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

    def test_is_empty(self):
        saved_user = User.objects.all()
        self.assertEqual(saved_user.count(), 0)

    def test_is_dummyuser_ja(self):
        self.setup_is_dummyuser(self.fake_ja, 1, 1, False)
        saved_user = User.objects.all()
        self.assertEqual(saved_user.count(), 1)

    def test_is_dummyuser_en(self):
        self.setup_is_dummyuser(self.fake_en, 1, 1, False)
        saved_user = User.objects.all()
        self.assertEqual(saved_user.count(), 1)

    def test_is_sameusername_ja(self):
        try:
            self.setup_is_dummyuser(self.fake_ja, 1, 2, False)
        except Exception:
            self.assertFalse(False)

    def test_is_sameusername_en(self):
        try:
            self.setup_is_dummyuser(self.fake_ja, 1, 2, False)
        except Exception:
            self.assertFalse(False)
