from datetime import datetime
from django.db import models
from AppGeneral.models import Status,Priorty
from AppProjectList.models import ProjectList

# Create your models here.

class TaskList(models.Model):
    strProjectName          = models.ForeignKey(ProjectList, on_delete=models.CASCADE, max_length=20)
    strTaskList             = models.TextField(max_length=100)
    strStatus               = models.ForeignKey(Status, on_delete=models.CASCADE, max_length=30)
    strPriorty              = models.ForeignKey(Priorty, on_delete=models.CASCADE, max_length=30)
    dueDateTask             = models.DateField(auto_now_add=False)
    dueDateProject          = models.DateField(auto_now_add=False)
    strNotes                = models.TextField(max_length=100)
    
    def __str__(self):
        if not self.strProjectName:
            return ""
        return str(self.strProjectName)
    
    

    
