from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    image = models.ImageField(upload_to='ads/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(60, 60)],
                                     format='JPEG',
                                     options={'quality': 90})
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    # Create your models here.
    class Meta:
        ordering = ['-created_date']
