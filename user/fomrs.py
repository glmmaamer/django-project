from django import forms
from django.contrib.auth.models import User

class create_account(forms.ModelForm):
    username   = forms.CharField(label='إسم المستخدم',max_length=30)
    email      = forms.CharField(label='إيمايل')
    first_name = forms.CharField(label='اللقب')
    last_name  = forms.CharField(label='الاسم')
    password1  = forms.CharField(label='كلمة السر',widget=forms.PasswordInput(),min_length=8)
    password2  = forms.CharField(label='تأكد كلمة السر',widget=forms.PasswordInput(),min_length=8)


    class Meta:
        model = User
        fields = ('username','email', 'first_name', 'last_name','password1','password2')