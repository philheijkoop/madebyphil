from django.shortcuts import render

from .models import Tag, Category, Post

def homepage(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    posts = Post.objects.all()
    context = {
        'category_list': categories,
        'tag_list': tags,
        'posts': posts,
    }
    return render(request, 'blog/homepage.html', context)

def post(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'blog/post.html', context)

def about(request):
    return render(request, 'blog/about.html')

def category_list(request):
    categories = Category.objects.all()
    context = {
        'category_list': categories
    }
    return render(request, 'blog/category_list.html', context)

def category_page(request, name):
    category = Category.objects.get(name=name)
    posts = Post.objects.filter(categories__in=[category])
    context = {
        'posts': posts
    }
    return render(request, 'blog/category_page', context)
    

def tag_list(request):
    tags = Tag.objects.all()
    context = {
        'tags': tags,
    }
    return render(request, 'blog/tag_list.html', context)

def tag_page(request, name):
    tag = Tag.objects.get(name=name)
    posts = Post.objects.filter(tags__in=[tag])
    context = {
        'posts': posts,
    }
    return render(request, 'blog/tag_page.html', context)

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)
