from django.urls import path, include

from .views import HomeView, PostView, AboutView, CategoryListView, CategoryPostListView, TagListView, TagPageView, AllPostView

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('blog/<slug>/', PostView.as_view(), name='post'),
    path('about/', AboutView.as_view(), name='about'),
    path('category/<name>/', CategoryPostListView.as_view(), name='categorypostlist'),
    path('tags/<name>/', TagPageView.as_view(), name='tagpage'),
    path('blog/', AllPostView.as_view(), name='allpostlist'),
    path('category/', CategoryListView.as_view(), name='categorylist'),
    path('tags/', TagListView.as_view(), name='taglist'),
    path('__debug__/', include('debug_toolbar.urls')),
]