
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm

from .models import TaskList
class TaskForm(ModelForm):
	class Meta:
		model = TaskList
		fields = "__all__"
            


