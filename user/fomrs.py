from django import forms
from django.contrib.auth.models import User
from .models import Profiles


#create accounte 
class create_account(forms.ModelForm):
    username   = forms.CharField(label='إسم المستخدم',max_length=30,help_text='إسم المستخدم يجب ان لايحتوي على مسافات')
    email      = forms.CharField(label='البريد الالكتروني')
    first_name = forms.CharField(label='اللقب')
    last_name  = forms.CharField(label='الاسم')
    password1  = forms.CharField(label='كلمة السر',widget=forms.PasswordInput(),min_length=8,help_text='كلمة السر لايجب ان تكون اقل من 8 أحرف أو ارقام أو رموز')
    password2  = forms.CharField(label='تأكد كلمة السر',widget=forms.PasswordInput(),min_length=8,help_text='كلمة السر التأكيد يجب ان تكون متطابقة مع كلمة السر الاولى')


    class Meta:
        model = User
        fields = ('username','email', 'first_name', 'last_name','password1','password2')


    #comparison two password 
    def comp_pass(self):
        c_data = self.cleaned_data
        if c_data['password1'] != c_data['password2']:
            raise forms.ValidationError('كلمة السر غير متطابقة')
        return c_data['password2']
    #comparison username
    def comp_username(self):
        c_user = self.cleaned_data
        if User.objects.filter(username=c_user['username']):
            raise forms.ValidationError('اسم المستخدم موجود')
        return c_user['username']
    

class LoginForm(forms.ModelForm):
    username  = forms.CharField(label='إضافة إسم المستخدم')
    password  = forms.CharField(label='إضافة كلمة المرور')
    class Meta:
        model = User
        fields = ('username','password')

class UpdateProfile(forms.ModelForm):
    email      = forms.CharField(label='البريد الالكتروني')
    first_name = forms.CharField(label='اللقب')
    last_name  = forms.CharField(label='الاسم')
    class Meta:
        model = User
        fields = ('email','first_name','last_name')

class Update_img_profile(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ('image',)
