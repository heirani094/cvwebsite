from django.contrib import admin
from blog.models import Post, Category, Advertisement


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'status', 'created_date', 'published_date')
    list_filter = ('status', 'created_date', 'published_date')
    ordering = ['-created_date']
    search_fields = ['title', 'content']


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'created_date')
    search_fields = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Advertisement, AdvertisementAdmin)
# Register your models here.
