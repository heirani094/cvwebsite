# Generated by Django 4.2.11 on 2024-07-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_rename_approach_comment_approved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='info@yahoo.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(default='ناشناس', max_length=255),
        ),
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
