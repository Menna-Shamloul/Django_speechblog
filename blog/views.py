from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView

# create data

posts = [
    {
        'author': 'Tarek Salah',
        'title' : 'Speech Blog Post',
        'content' : 'This my first post in this blog',
        'date_posted' : '1th January 2024',
    },
    {
        'author': 'Tom David',
        'title' : 'Speech Delay Blog Post',
        'content' : 'It is the first time to create post in speech blog',
        'date_posted' : '3th January 2024',
    }
]


# Create your views here.
# def home(request):
#   context = {
#       'posts': Post.objects.all()
#    }
#   return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ["date_posted"]
