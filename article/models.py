from django.db import models
from django.contrib.auth.models import User
from PIL import Image

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images')
    video = models.FileField(blank=True, null=True, upload_to='videos')
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title


