from django.urls import path

from . import views

app_name = "login"

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
]
