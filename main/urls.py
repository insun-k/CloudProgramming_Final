from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from main import views

urlpatterns = [
    path('', views.index),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('accounts/logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('accounts/signup/',views.signup, name='signup'),

]

