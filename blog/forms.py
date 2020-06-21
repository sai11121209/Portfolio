from django import forms
from .models import Posts
from mdeditor.fields import MDTextFormField # 追加

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'] = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'title', 'placeholder':'タイトル'}))
        self.fields['tags'] = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'tag', 'placeholder':'タグをスペース区切りで入力'}))
        self.fields['text'] =  MDTextFormField()

    class Meta:
        model = Posts
        fields = ('title', 'tags', 'text')
