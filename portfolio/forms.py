from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'title', 'text')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'氏名: 例)山田 太郎'}))
        self.fields['email'] = forms.EmailField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'メールアドレス: 例)portfolio@example.com ※任意'}))
        self.fields['title'] = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'件名: 件名を入力してください。'}))
        self.fields['text'] = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':'お問い合わせ内容: お問い合わせの内容をご入力ください。'}))

class ContactLoginForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('title', 'text')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'] = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'件名: 件名を入力してください。'}))
        self.fields['text'] = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':'お問い合わせ内容: お問い合わせの内容をご入力ください。'}))
