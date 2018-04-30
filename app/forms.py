from django import forms
from .models import User

class UserForm(forms.Form):
    username = forms.CharField(label = 'username', max_length=100)
    password = forms.CharField(label = 'password', max_length=100)

    class Meta:
        fields = ('username','password',)


    
