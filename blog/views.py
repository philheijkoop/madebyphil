from django.db.models import Count
from django.views import View
from django.views.generic.base import ContextMixin
from django.shortcuts import render

from .models import Tag, Category, Post

class CommonContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO sort the below filtered context objects by the correct metric
        category_list = Category.objects.annotate(number_of_post=Count('post')).filter(number_of_post__gt=0).order_by('-number_of_post')[:5]
        tags = Tag.objects.annotate(number_of_post=Count('post')).filter(number_of_post__gt=0).order_by('-number_of_post')[:5]
        posts = Post.objects.filter(published=True).order_by('publish_date')[:5]
        context['top_categories'] = category_list
        context['top_tags'] = tags
        context['top_posts'] = posts

        return context

class HomeView(View, CommonContextMixin):
    template_name  = "blog/homepage.html"
    def get(self, request):
        return render(request, self.template_name, context=self.get_context_data())
    
class PostView(View, CommonContextMixin):
    template_name = "blog/post.html"
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = self.get_context_data()
        context['post'] = post
        return render(request, self.template_name, context=context)

class AboutView(View, CommonContextMixin):
    def get(self, request):
        return render(request, 'blog/about.html', context=self.get_context_data())

class CategoryListView(View, CommonContextMixin):
    def get(self, request):
        context = self.get_context_data()
        categories = Category.objects.annotate(number_of_post=Count('post')).filter(number_of_post__gt=0).order_by('name')
        context['category_list'] = categories
        return render(request, 'blog/category_list.html', context)

class CategoryPostListView(View, CommonContextMixin):
    def get(self, request, name):
        context = self.get_context_data()
        category = Category.objects.get(name=name)
        category_posts = Post.objects.filter(category__in=[category]).filter(published=True)
        context['posts'] = category_posts
        return render(request, 'blog/category_post_list.html', context)

class TagListView(View, CommonContextMixin):
    def get(self, request):
        context = self.get_context_data()
        tags = Tag.objects.annotate(number_of_post=Count('post')).filter(number_of_post__gt=0).order_by('name')
        context['tags'] = tags
        return render(request, 'blog/tag_list.html', context)

class TagPageView(View, CommonContextMixin):
    def get(self, request, name):
        context = self.get_context_data()
        tag = Tag.objects.get(name=name)
        tag_posts = Post.objects.filter(tags__in=[tag]).filter(published=True)
        context['tag'] = tag
        context['posts'] = tag_posts
        return render(request, 'blog/tag_page.html', context)

class AllPostView(View, CommonContextMixin):
    def get(self, request):
        context = self.get_context_data()
        posts = Post.objects.filter(published=True)
        context['posts'] = posts
        return render(request, 'blog/all_posts.html', context)
