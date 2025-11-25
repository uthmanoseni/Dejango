# blog/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),        # http://127.0.0.1:8000/blog/
    path('home/', views.home_view, name='home2'),  # http://127.0.0.1:8000/blog/home/
    path('form/', views.form_view, name='form'),   # http://127.0.0.1:8000/blog/form/
]