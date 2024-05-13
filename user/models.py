from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profiles(models.Model):
    img = models.ImageField(default='default.jpg',upload_to='profile_picture')
    user = models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self):
        return '{}profile'.format(self.user.username)

def create_img(sender, **kwarg):
    if kwarg['created']:
        Profiles.objects.create(user=kwarg['instance'])

post_save.connect(create_img,sender=User)