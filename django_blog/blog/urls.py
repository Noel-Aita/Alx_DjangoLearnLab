from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # posts
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # auth
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
