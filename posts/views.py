from django.shortcuts import render, get_object_or_404

from .models import Post

def HomeView(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'posts/home.html', { 'posts': posts })

def PostDetailView(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', { 'post': post })
