from django.urls import path
from .views import HomePageView
from .views import Aboutpage

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/',Aboutpage.as_view(),name='about'),
]