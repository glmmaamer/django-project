from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date_post = models.DateTimeField(default=timezone.now)
    date_now = models.DateField(auto_now=True)
    user_post = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 
    
    class Meta:
        ordering = ('date_post', )
    
    