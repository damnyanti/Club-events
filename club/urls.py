from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('<club_Id>/', views.detail, name='detail'),
]