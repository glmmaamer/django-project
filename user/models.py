from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profil_pc(models.Model):
    img = models.ImageField(default='default.jpg',upload_to='profile_picture')
    user = models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self):
        return '{}profile'.format(self.user.username)
