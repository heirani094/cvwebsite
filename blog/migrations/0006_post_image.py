# Generated by Django 4.2.11 on 2024-06-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images', upload_to='blog/'),
        ),
    ]