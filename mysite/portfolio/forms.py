from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'title', 'txt')
        label = ('氏名', 'メールアドレス', '件名', 'ご意見・お問い合わせ')
        required = (True,False,True,True)
        widget = ('','',forms.Textarea,'')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(label='氏名', widget=forms.TextInput(attrs={'placeholder':'例)山田 太郎'}))
        self.fields['email'] = forms.EmailField(label='メールアドレス', required=False, help_text='※任意', widget=forms.TextInput(attrs={'placeholder':'例)portfolio@example.com'}))
        self.fields['title'] = forms.CharField(label='件名', widget=forms.TextInput(attrs={'placeholder':'件名を入力してください。'}))
        self.fields['txt'] = forms.CharField(label='ご意見・お問い合わせ', widget=forms.Textarea(attrs={'placeholder':'お問い合わせの内容をご入力ください。'}))

