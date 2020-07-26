from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('<club_id>/', views.detail, name='detail'),
]