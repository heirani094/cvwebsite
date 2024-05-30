from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank=True)
    content = models.TextField()
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
# Create your models here.
    class Meta:
        ordering = ['-created_date']