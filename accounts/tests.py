from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .views import *
from django.contrib.auth.models import User
from faker import Faker
from django.contrib.auth.hashers import make_password
from django.shortcuts import resolve_url
# Create your tests here.
class UserModelTest(TestCase):

    def setUp(self):
        self.fake_ja = Faker('ja_JP')
        self.fake_en = Faker()

    def setup_is_dummyuser(self, fake, N, M, su):
        users = []
        for i in range(N,M+1):
            dummy_deta = fake.profile()
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

    def test_is_accounts_signup(self):
        response = self.client.get(resolve_url('signup'))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Signup')
        self.assertContains(response, '登録')
        dummy_deta = self.fake_ja.profile()
        password = self.fake_ja.password(length=10)
        response = self.client.post(resolve_url('signup'), data={'username': dummy_deta['username'], 'password1': password, 'password2': password})
        self.assertEqual(302, response.status_code)
        saved_user = User.objects.all()
        self.assertEqual(saved_user.count(), 1)

    def test_is_accounts_mypage(self):
        response = self.client.get(resolve_url('mypage', username='None'))
        self.assertEqual(302, response.status_code)
        user = self.setup_is_dummyuser(self.fake_ja, 1, 2, False)
        rf = RequestFactory()
        request = rf.get(resolve_url('mypage', username=user[0]))
        request.user = user[0]
        response = MyPage(request, username=user[0].username)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'ログイン中(user)')
        self.assertContains(response, 'MyPage')
        self.assertContains(response, 'アカウント管理')
        request.user = user[0]
        response = MyPage(request, username=user[1].username)
        self.assertEqual(302, response.status_code,)

    def test_is_accounts_informationchange(self):
        response = self.client.get(resolve_url('information_change', username='None'))
        self.assertEqual(302, response.status_code)
        user = self.setup_is_dummyuser(self.fake_ja, 1, 2, False)
        rf = RequestFactory()
        request = rf.get(resolve_url('information_change', username=user[0]))
        request.user = user[0]
        response = UserInformationChange(request, username=user[0].username)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'ログイン中(user)')
        self.assertContains(response, 'InformationChange')
        self.assertContains(response, '変更')
        request.user = user[0]
        response = UserInformationChange(request, username=user[1].username)
        self.assertEqual(302, response.status_code,)
        dummy_deta = self.fake_ja.profile()
        request = rf.post(resolve_url('information_change', username=user[0].username), data={'email': dummy_deta['mail'], 'first_name': dummy_deta['name'].split()[1], 'last_name': dummy_deta['name'].split()[0]})
        request.user = user[0]
        response = UserInformationChange(request, username=user[0].username)
        self.assertEqual(302, response.status_code,)
        saved_user = get_object_or_404(User, pk=user[0].pk)
        self.assertEqual(saved_user.email, dummy_deta['mail'])