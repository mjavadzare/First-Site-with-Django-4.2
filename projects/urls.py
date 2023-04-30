from django.urls import path
from projects.views import *

app_name  = 'projects'

urlpatterns = [
    path('' , projects_view, name='index'),
    path('<int:pid>', projects_single_view, name='single'),
]
