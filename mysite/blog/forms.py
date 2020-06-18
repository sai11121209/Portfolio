from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'] = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'title', 'placeholder':'タイトル'}))
        self.fields['tag'] = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'tag', 'placeholder':'タグをスペース区切りで入力'}))
        self.fields['text'] = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'text', 'placeholder':'記入欄'}))

    class Meta:
        model = Posts
        fields = ('title', 'tag', 'text')
