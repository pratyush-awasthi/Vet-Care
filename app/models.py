from os import name
from django.db import models
from django.db.models.fields import CharField, DateTimeField, EmailField, TextField, URLField

class Appointment(models.Model):

    first_name = CharField(max_length=50)
    second_name = CharField(max_length=50)
    dog_name = CharField(max_length=50)
    detail = TextField()
    date = DateTimeField(auto_now=True)
    owner_name = CharField(max_length=25)
    breed = CharField(max_length=10) 
    image = models.ImageField(upload_to="appointments")
    email = EmailField()

    class Meta:

        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointment'

    def __str__(self):
        return self.dog_name

class Blog(models.Model):
    title = CharField(max_length=50)
    author_name = CharField(max_length=30)
    details = TextField()
    date = DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blogs')

    class Meta:

        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        
    def __str__(self):
        return self.title

class essentials(models.Model):
    name = CharField(max_length=50)
    description = CharField(max_length=250)
    image = models.ImageField(upload_to='essentials')

    class Meta:

        verbose_name = 'essentials'
        verbose_name_plural = 'essentials'

    def __str__(self):
        return self.name
