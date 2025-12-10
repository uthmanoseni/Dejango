# account/urls.py
from django.urls import path, include
from . import views
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import MyModelViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,

)
from .views import TestJWT, RegisterView, CustomLoginView

router = DefaultRouter()
router.register(r'mymodels', MyModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.newsletter_views, name='newsletter'),        # http://127.0.0.1:8000/account/
    path('newsletter/', views.newsletter_views, name='newsletter2'),  # http://127.0.0.1:8000/account/newsletter/
    path('aboutMe/', views.aboutMe_views,name='aboutMe'),  # http://127.0.0.1:8000/account/aboutMe/
    path('index/', views.index_views, name='index'),
    path('registration/signup/', views.signup_views, name='signup'),  # http://127.0.0.1:8000/account/signup/
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('registration/', include('django.contrib.auth.urls')), # Built-in auth URLs
    path('api/', include(router.urls)),
     # Signup
    path('signup/', RegisterView.as_view(), name='signup'),

        # JWT endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/test/', TestJWT.as_view(), name='test_jwt'),
]
