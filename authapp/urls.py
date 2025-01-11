from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.Home, name='Home' ),
    path('signup', views.signup, name='signup'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('contact', views.contact, name='contact'),
    path('join', views.enrollment, name='enrollment'),
    path('profile', views.profile, name='profile'),
    # path('gallery', views.gallery, name='gallery'),
    # path('getTrainer', views.getTrainer, name='getTrainer'),
]