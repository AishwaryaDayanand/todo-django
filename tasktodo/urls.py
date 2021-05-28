from django.urls import path
from .import views as task_views

urlpatterns = [
    # path('', task_views.index , name= "list"),
    path('', task_views.music , name= "song"),
    path('update_task/<str:pk>/', task_views.updateTask , name= "update_task"),
    path('delete_task/<str:pk>/', task_views.deleteTask , name= "delete_task"),

] 