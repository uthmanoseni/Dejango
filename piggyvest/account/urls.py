# account/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.newsletter_views, name='newsletter'),        # http://127.0.0.1:8000/account/
    path('newsletter/', views.newsletter_views, name='newsletter2'),  # http://127.0.0.1:8000/account/newsletter/
    path('aboutMe/', views.aboutMe_views,name='aboutMe'),  # http://127.0.0.1:8000/account/aboutMe/
]