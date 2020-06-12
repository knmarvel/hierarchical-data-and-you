from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', views.loginview, name="login"),
    path('logout/', views.logoutview, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('addfile/', views.add_file, name="addfile")
]
