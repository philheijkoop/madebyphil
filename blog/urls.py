from django.urls import path

from .views import homepage, post, post_list, tag_list, tag_page, category_list, category_page, about

urlpatterns = [
    path('', homepage, name='homepage'),
    path('blog/<slug>/', post, name='post'),
    path('about/', about, name='about'),
    path('category/<name>/', category_page, name='categorypage'),
    path('tags/<name>/', tag_page, name='tagpage'),
    path('blog/', post_list, name='allposts'),
    path('category/', category_list, name='categorylist'),
    path('tags/', tag_list, name='taglist'),
]