from django.urls import path

from .views import table, index

urlpatterns = [
    path('complite', table, name='index'),
    path('index', index, name='static'),

    ]

