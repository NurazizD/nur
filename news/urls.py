from django.urls import path
from .views import news,BlogDetailView
from django.conf.urls.static import static 
urlpatterns = [
    path('',news.as_view(),name='news'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
]