from django.urls import path

from .views import homepage, post, category_post_list, tag_list, tag_page, category_list, about, allposts

urlpatterns = [
    path('', homepage, name='homepage'),
    path('blog/<slug>/', post, name='post'),
    path('about/', about, name='about'),
    path('category/<name>/', category_post_list, name='postlist'),
    path('tags/<name>/', tag_page, name='tagpage'),
    path('blog/', allposts, name='allpostlist'),
    path('category/', category_list, name='categorylist'),
    path('tags/', tag_list, name='taglist'),
]