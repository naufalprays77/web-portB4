from datetime import datetime
from django.db import models
from AppGeneral.models import Status,Priorty

# Create your models here.
    
class ProjectList(models.Model):
    strIDProject            = models.TextField(max_length=20)
    strProjectName          = models.TextField(max_length=100)
    strProjectDescription   = models.TextField(max_length=100)
    strStatus               = models.ForeignKey(Status, on_delete=models.CASCADE, max_length=30)
    strPriorty              = models.ForeignKey(Priorty, on_delete=models.CASCADE, max_length=30)
    datetimeStartProject    = models.DateField(auto_now_add=False)
    dueDateTimeProject      = models.DateField(auto_now_add=False)
    strNotes                = models.TextField(max_length=100)
    
    # def __str__(self):
    #     return "{} {}".format( self.strIDProject, self.strProjectName) 
    def __str__(self):
        return self.strProjectName 
    
    def __str__(self):
        return self.strIDProject 
        
    