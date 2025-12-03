# blog/urls.py
from django.urls import path
from . import views
from .views import product_list, catalogue_list # For Class-Based View


urlpatterns = [
    path('', views.home_view, name='home'),        # http://127.0.0.1:8000/blog/
    path('home/', views.home_view, name='home2'),  # http://127.0.0.1:8000/blog/home/
    path('form/', views.form_view, name='form'),   # http://127.0.0.1:8000/blog/form/
    # Product URLs
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/update/<int:pk>/', views.product_update, name='product_update'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),

    # Catalogue URLs
    path('catalogues/', views.catalogue_list, name='catalogue_list'),
    path('catalogues/create/', views.catalogue_create, name='catalogue_create'),
    path('catalogues/update/<int:pk>/', views.catalogue_update, name='catalogue_update'),
    path('catalogues/delete/<int:pk>/', views.catalogue_delete, name='catalogue_delete'),
]