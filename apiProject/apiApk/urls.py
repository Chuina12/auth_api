from django.urls import path 
from . import views 

app_name = 'apiApk'
urlpatterns = [
  path('create-user', views.asyncCreateUser, name='create-user'),
  path('conpte', views.conpte),
    
]
