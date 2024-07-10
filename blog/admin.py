# admin.py
from django.contrib import admin
from blog.models import Post, Category, Advertisement, Comment
from django_summernote.admin import SummernoteModelAdmin


# class PostAdmin(admin.ModelAdmin):
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'status', 'created_date', 'published_date')
    list_filter = ('status', 'created_date', 'published_date')
    ordering = ['-created_date']
    search_fields = ['title', 'content']
    summernote_fields = ('content',)  # Specify the fields to use Summernote


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'created_date')
    search_fields = ('title',)


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'approved', 'created_date')
    list_filter = ('post', 'approved')
    search_fields = ['name', 'post__title']


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Advertisement, AdvertisementAdmin)
# Register your models here.
