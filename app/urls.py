from os import name
from django.urls import path
from django.views.generic import TemplateView
from app import views

urlpatterns = [
    path('',views.blogs_home_view, name='index'),
    path('appointment/book',views.book_appointment, name='book_appointment'),
    path('blogs/view',views.blogs_view, name='blog'),
    path('blog/new',views.new_blog, name='new_blog'),
    path('blog/detail/<int:id>/',views.detailed_blogs, name='detailed_blog'),
    path('blog/delete/<int:id>/',views.blog_delete, name="blog_delete"),
    path('blog/edit/<int:id>/',views.blog_edit, name="edit_blog"),
    path('search/',views.search_blog,name="search"),
]

