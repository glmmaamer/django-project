from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image

# Create your models here.

class Profiles(models.Model):
    image = models.ImageField(default='default.jpg',upload_to='profile_picture')
    user = models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self):
        return '{}profile'.format(self.user.username)
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.width >300 or img.height >300:
            size_img = (300,300)
            img.thumbnail(size_img)
            img.save(self.image.path)
        
        

def create_img(sender, **kwarg):
    if kwarg['created']:
        Profiles.objects.create(user=kwarg['instance'])

post_save.connect(create_img,sender=User)