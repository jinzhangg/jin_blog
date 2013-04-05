from django.shortcuts import render_to_response
from jin_blog.models import Post, Page

def home(request):
    posts = Post.objects.filter(published=True)
    return render_to_response("home.html", dict(posts=posts))

def about(request):
    page = Page.objects.get(title="About")
    return render_to_response("about.html", dict(page=page))

def contact(request):
    page = Page.objects.get(title="Contact")
    return render_to_response("contact.html", dict(page=page))