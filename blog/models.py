from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.



class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date_post = models.DateTimeField(default=timezone.now)
    date_now = models.DateField(auto_now=True)
    user_post = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        #return '/detail/{}'.format(self.pk)
        return reverse('detail', args=[self.pk])
    
    class Meta:
        ordering = ('date_post', )


class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='الاسم')
    email = models.EmailField(verbose_name='البريد الالكتروني')
    body = models.TextField(verbose_name='تعليق جديد')
    active = models.BooleanField(default=False)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return 'علق {} على {}.'.format(self.name, self.post)
    