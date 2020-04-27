from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True,null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(max_length=250)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    current_location = models.CharField(max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
