from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.urls import reverse
from taggit.managers import TaggableManager
# from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field


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
    # content = models.TextField()
    content = CKEditor5Field('Content', config_name='default')
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)
    category = models.ManyToManyField(Category)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    # Create your models here.
    class Meta:
        ordering = ['-created_date']

    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid': self.id})
