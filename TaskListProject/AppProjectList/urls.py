from django.urls import path

from .views import *
app_name='projectList'

urlpatterns = [
	path('<int:pk>/delete/', DeleteProjectList.as_view(), name='delete'),
    path('<int:pk>/update/', UpdateProjectList.as_view(), name='update'),
	path('<int:pk>/detail/', DetailProjectList.as_view(), name='detail'),
	path('', ListProject.as_view(), name='index'),
	path('create', CreateProjectList.as_view(), name='create'),
]

    