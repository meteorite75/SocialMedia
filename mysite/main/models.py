from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    first_name = models.CharField(max_length=100 , default='first_name')
    last_name = models.CharField(max_length=100, default='last_name')
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images' , default='default_pic.png')
    location = models.CharField(max_length= 100, blank= True)
    
    def __str__(self):
        return self.user.username
    
class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    followed_user = models.CharField(max_length=100)
    
    def __str__(self):
        return self.follower