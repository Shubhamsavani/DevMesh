from django.urls import path
from . import views
# the defination i.e the functions are kept in the views folder so the above line connects the views.py and this file


urlpatterns = [
    path('', views.projects, name='projects'),#GIVING NO ARGUMENTS IN THE URL PATH WILL MAKE THIS URL PAGE OUR HOME/DEFAULT PAGE
    #path('projects/', views.projects, name='projects'),#make a url path 
    path('project/<str:pk>', views.project,name='project'), #this url will also take a string along with it so that we can use it in thwe  fucntion
    path('create-project/', views.create_project,name='project_form'),
    path('edit-project/<str:pk>', views.edit_project, name='edit-project'),
    path('delete-project/<str:pk>', views.delete_project, name='delete-project'),
]
