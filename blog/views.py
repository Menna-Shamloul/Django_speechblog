from django.shortcuts import render
from django.http import HttpResponse

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
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
