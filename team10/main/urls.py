# main/urls.py
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('chat', views.chat, name='chat'),
    path('', views.test),
    path('policySvcMain/', views.get_policySvcMain),
    path('privateMain/', views.get_privateMain),
    
    #display both cameras
    path('bycv2/', views.index, name='index'),

    #access the laptop camera
    path('video_feed/', views.video_feed, name='video_feed'),

    #access the phone camera
    path('webcam_feed/', views.webcam_feed, name='webcam_feed'),

]