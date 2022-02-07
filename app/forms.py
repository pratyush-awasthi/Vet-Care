from django import forms
from .models import Appointment, Blog


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('first_name','second_name','email','dog_name','detail','owner_name','breed','image')
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','author_name','details','image')