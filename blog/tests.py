from django.test import TestCase, RequestFactory
from .models import Posts
from .views import *
from django.contrib.auth.models import User
from faker import Faker
from django.contrib.auth.hashers import make_password
from django.shortcuts import resolve_url
# Create your tests here.

class PostsModelTest(TestCase):
    def test_is_empty(self):
        saved_posts = Posts.objects.all()
        self.assertEqual(saved_posts.count(), 0)

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

    def setup_is_dummyposts(self, fake, N):
        dummy_deta = fake.profile()
        posts = []
        for i in range(1,N+1):
            posts.append(Posts.objects.create(
                id=i,
                author_id=1,
                title=dummy_deta['company'],
                tags=dummy_deta['name'],
                text=dummy_deta['residence'],
                created_date=fake.date_time_ad(),
                update_date=fake.date_time_ad(),
            ))
        return posts

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

    def test_is_blog_home(self):
        response = self.client.get(resolve_url('blog:home'))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Blog')
        self.assertContains(response, '最新記事')
        self.assertEqual(None, response.context['username'].id)
        user = self.setup_is_dummyuser(self.fake_ja, 1, 1, False)[0]
        rf = RequestFactory()
        request = rf.get(resolve_url('blog:home'))
        request.user = user
        response = Blog(request)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'ログイン中(user)')
        user = self.setup_is_dummyuser(self.fake_ja, 2, 2, True)[0]
        rf = RequestFactory()
        request = rf.get(resolve_url('blog:home'))
        request.user = user
        response = Blog(request)
        self.assertEqual(200, response.status_code,)
        self.assertContains(response, 'ログイン中(admin)')

    def test_is_blog_post(self):
        response = self.client.get(resolve_url('blog:post'))
        self.assertEqual(302, response.status_code)
        dummy_deta = self.fake_ja.profile()
        user = self.setup_is_dummyuser(self.fake_ja, 1, 1, False)[0]
        rf = RequestFactory()
        request = rf.post(resolve_url('blog:post'), data={'title': dummy_deta['company'],'tags': dummy_deta['name'], 'text': dummy_deta['residence']})
        request.user = user
        response = Post(request)
        self.assertEqual(302, response.status_code)
        saved_posts = Posts.objects.all()
        self.assertEqual(saved_posts.count(), 1)

    def test_is_blog_postlist(self):
        response = self.client.get(resolve_url('blog:list'))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'PostList')
        self.assertContains(response, '記事一覧')
        self.assertEqual(None, response.context['username'].id)
        user = self.setup_is_dummyuser(self.fake_ja, 1, 1, False)[0]
        rf = RequestFactory()
        request = rf.get(resolve_url('blog:list'))
        request.user = user
        response = Blog(request)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'ログイン中(user)')
        user = self.setup_is_dummyuser(self.fake_ja, 2, 2, True)[0]
        rf = RequestFactory()
        request = rf.get(resolve_url('blog:list'))
        request.user = user
        response = PostList(request)
        self.assertEqual(200, response.status_code,)
        self.assertContains(response, 'ログイン中(admin)')

    def test_is_blog_postdetail(self):
        user = self.setup_is_dummyuser(self.fake_ja, 1, 2, False)
        post = self.setup_is_dummyposts(self.fake_ja, 1)[0]
        response = self.client.get(resolve_url('blog:detail', pk=post.pk, author=post.author))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'PostDetail')
        self.assertContains(response, post.title)
        rf = RequestFactory()
        request = rf.get(resolve_url('blog:detail', pk=post.pk, author=post.author))
        request.user = user[0]
        response = PostDetail(request, pk=post.pk, author=post.author)
        self.assertEqual(200, response.status_code,)
        self.assertContains(response, 'ログイン中(user)')
        self.assertContains(response, '編集')
        request.user = user[1]
        response = PostDetail(request, pk=post.pk, author=post.author)
        self.assertEqual(200, response.status_code,)
        self.assertContains(response, 'ログイン中(user)')