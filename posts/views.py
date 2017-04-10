from django.shortcuts import render

from .models import Post

def HomeView(request):
    posts = Post.objects.order_by('pub_date')
    print('hi')

    return render(request, 'posts/home.html', { 'posts': posts })
