# Generated by Django 4.2.11 on 2024-07-09 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_tags_alter_post_content_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approach',
            new_name='approved',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='Post',
            new_name='post',
        ),
    ]