from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from jin_blog.models import Post, Page

def home(request):
    post_list = Post.objects.filter(published=True)
    # Show 5 posts per page
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render_to_response("home.html", dict(posts=posts))

def about(request):
    page = get_object_or_404(Page, title="About")
    return render_to_response("about.html", dict(page=page))

def contact(request):
    page = get_object_or_404(Page, title="Contact")
    return render_to_response("contact.html", dict(page=page))

def single_post(request, pk):
    post = get_object_or_404(Post, pk=pk, published=True)
    return render_to_response("single_post.html", dict(post=post))
