# Generated by Django 3.2.4 on 2021-07-20 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_display_name_blog_author_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='essentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='essentials')),
            ],
            options={
                'verbose_name': 'essentials',
                'verbose_name_plural': 'essentials',
            },
        ),
    ]
