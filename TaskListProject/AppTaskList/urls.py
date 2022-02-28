from django.urls import path

from .views import *
app_name='taskList'

urlpatterns = [
	path('<int:pk>/delete/', DeleteTasktList.as_view(), name='delete'),
    path('<int:pk>/update/', UpdateTaskList.as_view(), name='update'),
	path('<int:pk>/detail/', DetailTaskList.as_view(), name='detail'),
	path('', TaskProject.as_view(), name='index'),
	path('create', CreateTaskList.as_view(), name='create'),
]

    