from django.urls import path
from django.views.generic import RedirectView
from . import views
urlpatterns = [
    path('', views.index, name='home.index'),
    path('home/', RedirectView.as_view(pattern_name='home.index')),
    path('about', views.about, name='home.about'),
]
