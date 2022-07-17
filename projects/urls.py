from django.urls import path

from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    #read
    path('project/<str:pk>/', views.project, name='project'),
    #create
    path('create-project/', views.create_project, name='create-project'),
    #update
    path('update-project/<str:pk>', views.update_project, name='update-project'),
    #delete
    path('delete-project/<str:pk>', views.delete_project, name='delete-project'),
]
