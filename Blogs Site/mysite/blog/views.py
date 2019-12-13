from django.shortcuts import render, HttpResponse
from blog.models import Post

# Create your views here.
def blog(request):
    Allpost = Post.objects.filter(status=1).order_by('-timestamp')
    return render(request, "blog/blog-home.html", {'Allpost':Allpost})

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    return render(request, "blog/blog-page.html", {"post": post}) 