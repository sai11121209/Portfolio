from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UsernameChangeForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
import sys
sys.path.append('../')
from blog.models import Posts
from portfolio.models import Contact

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

@login_required
def MyPage(request):
    postlists = Posts.objects.filter(author=request.user)
    contactlists = Contact.objects.filter(name=request.user)
    print(postlists)
    return render(request, 'registration/mypage.html', {'username': request.user, 'postlists': postlists, 'contactlists': contactlists})

@login_required
def UserInformationChange(request, username):
    form = UsernameChangeForm(request.POST or None)
    if get_object_or_404(User, username=username).username == str(request.user):
        user = get_object_or_404(User, username=username)
        form.fields['first_name'].widget = forms.TextInput(attrs={'value': user.first_name})
        form.fields['last_name'].widget = forms.TextInput(attrs={'value': user.last_name})
        form.fields['email'].widget = forms.TextInput(attrs={'value': user.email})
        if request.method == 'POST' and form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('mypage')
        return render(request, 'registration/information_change_form.html', {'username': request.user, 'form': form})
    return redirect('mypage')