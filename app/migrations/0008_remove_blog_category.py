# Generated by Django 3.2.4 on 2021-07-28 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_blog_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
    ]
