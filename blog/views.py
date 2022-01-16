from django.http import request
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, PublishedManager
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def postList(request):
    posts=Post.objects.filter(status='1')
    latest_posts=Post.objects.filter(status='1')[:5]
    
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    context = {'posts': posts, 'page_title': 'Blog', 'latest_posts': latest_posts, 'page': page}
    return render(request, 'novi_blog.html', context)

    
def postDetail(request, year, month, day, post):
    latest_posts=Post.objects.all()[:5]
    post = get_object_or_404(Post, slug=post, status='1', created_at__year=year, created_at__month=month, created_at__day=day)
    return render(request, 'blog/blog_post.html', {'post': post, 'latest_posts': latest_posts, 'page_title': 'Blog' })