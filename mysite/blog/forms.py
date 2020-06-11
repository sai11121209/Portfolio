from django import forms
from .models import Post, User
from django.contrib.auth.hashers import make_password

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'] = forms.CharField(label='タイトル', widget=forms.TextInput(attrs={'placeholder':'タイトル'}))
        self.fields['tag'] = forms.CharField(label='タグ', widget=forms.TextInput(attrs={'placeholder':'タグをスペース区切りで入力'}))
        self.fields['text'] = forms.CharField(label='本文', widget=forms.Textarea(attrs={'placeholder':'記入欄'}))

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'tag')




class RegisterForm(forms.Form):
    username = forms.CharField(label='ユーザネーム', widget=forms.TextInput(attrs={'placeholder':'タイトル'}))
    email = forms.EmailField(label='メールアドレス', widget=forms.TextInput(attrs={'placeholder':'例)portfolio@example.com'}))
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput(attrs={'placeholder':'パスワード'}))
    repassword = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput(attrs={'placeholder':'パスワード再入力'}))