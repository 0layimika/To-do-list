from django.contrib import admin
from django.urls import path
from . import views
from .views import *
app_name='jobs'
urlpatterns = [
    path('create_job/',JobsCreateView.as_view(),name='create_job'),
    path('jobs_list/',JobsListView.as_view(),name='jobs_list'),
    path('jobs_detail/<int:pk>',JobsDetailView.as_view(),name='jobs_detail'),
    path('delete_job/<int:pk>',JobsDeleteView.as_view(),name='delete_job')
]