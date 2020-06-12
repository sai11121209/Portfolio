from django.shortcuts import render, redirect
from django import forms
from .models import User
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
"""
def register(request):
    form = RegisterForm(request.POST or None)
    form.fields['password'].widget = forms.PasswordInput(attrs={'placeholder':'パスワード'})
    form.fields['repassword'].widget = forms.PasswordInput(attrs={'placeholder':'パスワード再入力'})
    print(request.method)
    if request.method == 'POST' and form.is_valid():
        print('a')
        if form.cleaned_data['password'] == form.cleaned_data['repassword']:
            user = User.objects.create (
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=make_password(form.cleaned_data['password']),
            )
            login(request, user)
            return redirect('login')
        return redirect('register')
    return render(request, 'blog/register.html', {'form':form})


def login(request):
    form = LoginForm(request.POST or None)
    form.fields['password'].widget = forms.PasswordInput(attrs={'placeholder':'パスワード'})
    if request.method == 'POST' and form.is_valid():
        if User.objects.filter(email=form.cleaned_data['email']).exists():
            users = User.objects.filter(email=form.cleaned_data['email']).values()
            if check_password(form.cleaned_data['password'],users[0]['password']):
                return redirect('post')
        return redirect('login')
    return render(request, 'blog/login.html', {'form': form})
"""
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def User(request):
    print(request.user)
    return redirect('login')