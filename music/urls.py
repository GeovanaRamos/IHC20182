from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('', views.MyMusicView.as_view(), name='my_music'),
]