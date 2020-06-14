from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'] = forms.CharField(label='タイトル', widget=forms.TextInput(attrs={'placeholder':'タイトル'}))
        self.fields['text'] = forms.CharField(label='本文', widget=forms.Textarea(attrs={'placeholder':'記入欄'}))
        self.fields['tag'] = forms.CharField(label='タグ', widget=forms.TextInput(attrs={'placeholder':'タグをスペース区切りで入力'}))

    class Meta:
        model = Posts
        fields = ('title', 'tag', 'text')
