from django import forms
from .models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'tag')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'] = forms.CharField(label='タイトル', widget=forms.TextInput(attrs={'placeholder':'タイトル'}))
        self.fields['tag'] = forms.CharField(label='タグ', widget=forms.TextInput(attrs={'placeholder':'タグをスペース区切りで入力'}))
        self.fields['text'] = forms.CharField(label='本文', widget=forms.Textarea(attrs={'placeholder':'記入欄'}))


class RegisterForm(forms.ModelForm):
    class Meta:
        pass