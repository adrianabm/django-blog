from django.shortcuts import render

def HomeView(request):
    return render(request, 'posts/home.html')
