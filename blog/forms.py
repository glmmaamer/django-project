from django import forms
from  .models import Comment, Post


class NowComment(forms.ModelForm):
       
       class Meta:
        model = Comment
        fields = ('name','email','body')

class post_ar(forms.ModelForm):
    name = forms.CharField(label='إسم التدوينة')
    description = forms.CharField(label='وصف التدوينة',widget=forms.Textarea)
    class Meta:
        model = Post
        fields =  ['name','description']
       
    