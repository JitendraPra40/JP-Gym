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
    path('gallery', views.gallery, name='gallery'),
    path('services', views.service, name='service'),
    path('attendance', views.attendance, name='attendance'),
    path('about', views.about_us, name='about_us'),
    path('service', views.service, name='service'),
    path('reviews', views.reviews, name='reviews')
]