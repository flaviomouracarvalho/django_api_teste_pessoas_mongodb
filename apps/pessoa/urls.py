
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="lista-pessoas"),
    path('create_pessoa/', views.create_pessoa, name="create-pessoa"),
    path('delete_pessoa/', views.delete_pessoa, name="delete-pessoa"),
    path('update_pessoa/', views.update_pessoa, name="update-pessoa"),
]
