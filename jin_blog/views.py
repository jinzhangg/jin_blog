from django.shortcuts import render_to_response
from jin_blog.models import Post

def home(request):
    posts = Post.objects.filter(published=True)
    return render_to_response("home.html", dict(posts=posts))

def about(request):
    return render_to_response("about.html")

def contact(request):
    return render_to_response("contact.html")