from django import forms
from .models import Contact

class UserForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            'name': '名前',
            'mail_address': '年齢',
            'title': '件名',
            'txt': '本文',
        }
        help_texts = {
            'name': '名前',
            'mail_address': '年齢',
            'title': '件名',
            'txt': '本文',
        }