from django.urls import path
from .views import SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]