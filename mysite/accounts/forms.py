from django import forms
from django.contrib.auth.models import User
"""
class RegisterForm(forms.Form):
    username = forms.CharField(label='ユーザネーム', widget=forms.TextInput(attrs={'placeholder':'ユーザーネーム'}))
    email = forms.EmailField(label='メールアドレス', widget=forms.TextInput(attrs={'placeholder':'例)portfolio@example.com'}))
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput(attrs={'placeholder':'パスワード'}))
    repassword = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput(attrs={'placeholder':'パスワード再入力'}))


class LoginForm(forms.Form):
    email = forms.EmailField(label='メールアドレス', widget=forms.TextInput(attrs={'placeholder':'メールアドレス'}))
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput(attrs={'placeholder':'パスワード'}))
"""

class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')