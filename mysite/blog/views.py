from django.shortcuts import render, redirect
from django import forms
from .forms import PostForm, RegisterForm
from .models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        form.fields['password'].widget = forms.PasswordInput(attrs={'placeholder':'パスワード'})
        form.fields['repassword'].widget = forms.PasswordInput(attrs={'placeholder':'パスワード再入力'})
        print(form)
        if form.is_valid:
            if form.fields['password'] == form.fields['repassword']:
                User.objects.create (
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=make_password(form.cleaned_data['password']),
                )
        return redirect('login')
    else:
        form = RegisterForm()
        return render(request, 'blog/register.html', {'form':form})


def login(request):
    return render(request, 'blog/login.html')


def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        print('a')
        if form.is_valid():
            form.save()
            print('a')
        return redirect('post')
    else:
        form = PostForm()
    return render(request, 'blog/post.html', {'form': form})
