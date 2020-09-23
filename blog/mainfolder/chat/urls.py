from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.chat),
    path('<str:room_name>/', views.room, name='room')

]
