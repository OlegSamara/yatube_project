from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/', views.groups),
    path('group/<slug:all_slug>/', views.group_posts)
]
