from django.shortcuts import render_to_response
from jin_blog.models import Post

def home(request):
    posts = Post.objects.filter(published=True)

    return render_to_response("home.html", dict(posts=posts))