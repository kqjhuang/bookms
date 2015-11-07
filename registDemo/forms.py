#coding:utf-8
from django import forms
from .models import *

class UserForm(forms.Form):
    username = forms.CharField(label='帐号', max_length=20)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

class PersonForm(forms.ModelForm):
	
    class Meta:
        model = Person	
        exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

