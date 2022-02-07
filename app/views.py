from django.db.models.fields import DateTimeField
from django.shortcuts import redirect, render
from .models import Appointment, Blog, essentials
from .forms import AppointmentForm, BlogForm
from django.contrib import messages

def book_appointment(request):
    
    if request.method == "POST":
        form = AppointmentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Appointment successfully booked, you will get the date and time through email .')
            return redirect('book_appointment')
        else:
            messages.error(request,'Appointment could not be booked.')
    else:
        form = AppointmentForm()
    ctx = {
        "form": form,
        "title":"Book new Appointment"
    }
    return render(request,"book_appointment.html",ctx)


def new_blog(request):
    
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'New Blog successfully posted.')
            return redirect('new_blog')
        else:
            messages.error(request,'New Blog could not be posted.')
    else:
        form = BlogForm()
    ctx = {
        "form": form,
        "title":"Add new Blog"
    }
    return render(request,"new_blog.html",ctx)

def blogs_view(request):
    blogs = Blog.objects.all()
    ctx = {
        'title':"All Blogs",
        'blogs': blogs,
    }
    return render(request,"blog.html",ctx)

def blogs_home_view(request):
    blogs = Blog.objects.order_by('date')[:3:-1]
    Essentials = essentials.objects.all()
    ctx = {
        'title':"Home",
        'blogs': blogs,
        'essentials': Essentials,
    }

    return render(request,"index.html",ctx)
    

def detailed_blogs(request,id):
    try:
        blogs = Blog.objects.get(id=id)
        ctx ={
            'title':"Detailed Blog",
            'blogs':blogs
        }
        return render(request,"detailed_blog.html",ctx)
    except:
        return redirect("blog")

def blog_delete(request,id):
    try:
        Blog.objects.get(id=id).delete()
        messages.success(request,"Blog deleted successfully")
        return redirect("blog")
    except Exception as e:
        print(e)
        messages.error(request,"Blog could not be deleted!")
        return redirect("detailed_blog",id=id)

def blog_edit(request,id):
    try:
        blog = Blog.objects.get(id=id)
        if request.method == "POST":
            form = BlogForm(request.POST,request.FILES,instance=blog)
            if form.is_valid():
                form.save()
                messages.success(request,"Blog updated successfully")
                return redirect("detailed_blog",id=id)
            else:
                messages.error(request,"Blog update error")
        else:
            form = BlogForm(instance=blog)
        ctx = {
            'title':"Edit your Blog",
            'form':form,
            'id':id,
        }
        return render(request,"edit_blog.html",ctx)
    except Exception as e:
        print(e)
        return redirect("blog")

def search_blog(request):
    q = request.GET.get('query')
    if q:
        results = Blog.objects.filter(title__contains=q)
        print(results)
        if len(results)>0:
            ctx = {
                'title':'Search Results',
                'results':results,
                'query':q,
            }
            return render(request, "search.html",ctx)
    return redirect('index')