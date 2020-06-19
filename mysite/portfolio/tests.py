from django.test import TestCase, RequestFactory
from .models import Contact
from .views import Portfolio
from django.contrib.auth.models import User
from faker import Faker
from django.contrib.auth.hashers import make_password
from django.shortcuts import resolve_url

# Create your tests here.
class ContactModelTest(TestCase):

    def setUp(self):
        self.fake_ja = Faker('ja_JP')
        self.fake_en = Faker()

    def test_is_empty(self):
        saved_contact = Contact.objects.all()
        self.assertEqual(saved_contact.count(), 0)

    def setup_is_dummycontact(self, fake, N):
        dummy_deta = fake.profile()
        for i in range(1,N+1):
            Contact.objects.create(
            id=i,
            name=dummy_deta['name'],
            email=dummy_deta['mail'],
            title=dummy_deta['company'],
            text=dummy_deta['residence'],
            created_date=fake.date_time_ad(),
            update_date=fake.date_time_ad(),
            )

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

    def test_is_dummycontact_ja(self):
        self.setup_is_dummycontact(self.fake_ja, 1)
        saved_contact = Contact.objects.all()
        self.assertEqual(saved_contact.count(), 1)

    def test_is_dummycontact_en(self):
        self.setup_is_dummycontact(self.fake_en, 1)
        saved_contact = Contact.objects.all()
        self.assertEqual(saved_contact.count(), 1)

    def test_is_portfolio(self):
        response = self.client.get(resolve_url('portfolio:home'))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Portfolio')
        self.assertContains(response, '氏名')
        self.assertEqual(None, response.context['username'].id)
        user = self.setup_is_dummyuser(self.fake_ja, 1, 1, False)[0]
        rf = RequestFactory()
        request = rf.get(resolve_url('portfolio:home'))
        request.user = user
        response = Portfolio(request)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'ログイン中(user)')
        self.assertContains(response, 'アカウントの情報を使用するため省略。')
        user = self.setup_is_dummyuser(self.fake_ja, 2, 2, True)[0]
        rf = RequestFactory()
        request = rf.get(resolve_url('portfolio:home'))
        request.user = user
        response = Portfolio(request)
        self.assertEqual(200, response.status_code,)
        self.assertContains(response, 'ログイン中(admin)')
        self.assertContains(response, 'アカウントの情報を使用するため省略。')
        dummy_deta = self.fake_ja.profile()
        request = rf.post(resolve_url('portfolio:home'), data={'title': dummy_deta['company'], 'text': dummy_deta['residence']})
        request.user = user
        response = Portfolio(request)
        print(response)
        self.assertEqual(302, response.status_code)
        saved_contact = Contact.objects.all()
        self.assertEqual(saved_contact.count(), 1)