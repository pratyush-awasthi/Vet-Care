# Generated by Django 3.2.4 on 2021-07-20 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_bread_appointment_breed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='display_name',
            new_name='author_name',
        ),
    ]
