from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dash, name="dash"),
    path('reward/', views.reward, name="reward"),
    path('add_views/', views.create_views, name="create_views"),
    path('reward/', views.reward, name="reward"),
    path('earn_points/', views.earn_points, name="earn_points"),
    path('earn_points/<str:cat>/', views.category, name="category"),
    path('watch_video/<str:video_id>/', views.watch_video, name="watch_video"),
    path('my_videos/', views.my_videos, name="my_videos"),
]
