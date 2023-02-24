from django.urls import path

from . import views

app_name = 'group'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/', views.groups, name='groups'),
    path('group/<slug:all_slug>/', views.group_posts, name='group_posts')
]
