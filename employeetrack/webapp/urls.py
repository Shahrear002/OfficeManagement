from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('userhome/', views.userhome, name='userhome'),
    path('logout/', views.logout_view)
]
