from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Маршрут для списка постов
]
