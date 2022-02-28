
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm

from .models import ProjectList
class ProjectForm(ModelForm):
	class Meta:
		model = ProjectList
		fields = '__all__'
            


