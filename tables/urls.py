from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.login_user, name='login'), # <--- use this if you are creating seperate page for loggin in
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]
