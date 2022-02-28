from ast import parse
from lib2to3.pytree import convert
from xml.dom.expatbuilder import parseString
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models.functions import Substr 

from AppGeneral.models import *
from AppProjectList.forms import ProjectForm
from .models import ProjectList
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView,
    DeleteView
)

class ListProject(ListView):
    model = ProjectList
    template_name = 'ProjectList/index.html'
    context_object_name = 'projectList'
    ordering = ['strIDProject']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['strStatus'] = Status.objects.all()
        context['strPriorty'] = Priorty.objects.all()
        context['strProjectName'] = ProjectList.objects.all()
        return context
    
class CreateProjectList(CreateView):
    Model=ProjectList
    form_class = ProjectForm
    template_name = 'ProjectList/create.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['strStatus'] = Status.objects.all()
        context['strPriorty'] = Priorty.objects.all()
        IDProject=ProjectList.objects.last()
        strIDProject=str(IDProject)
        sliceIDProject=strIDProject[2:5]
        intIDProject=int(sliceIDProject)+1
        if intIDProject < 10 :
            newstrIDProject="ID00"+str(intIDProject)
        elif intIDProject > 99:
            newstrIDProject="ID"+str(intIDProject)
        else:
            newstrIDProject="ID0"+str(intIDProject)

        context['strIDProject'] = newstrIDProject
        return context
    
    def post(self, request):
        if request.method == 'POST':
            self.form = ProjectForm(self.request.POST)
            print(ProjectForm(self.request.POST))
            if self.form.is_valid():
                self.form.save()
                return redirect('projectList:index')
            return super().form_valid(self.form)

class DeleteProjectList(DeleteView):
	model = ProjectList
	template_name = 'ProjectList/confirm_delete.html'
	success_url = reverse_lazy('projectList:index')

class DetailProjectList(DetailView):
#for detail by id
	Model=ProjectList
	form_class = ProjectForm
	template_name = "ProjectList/detail.html"

	def get(self, *args, **kwargs):
		data_detail = ProjectList.objects.get(id=kwargs['pk'])
		data = data_detail.__dict__
		self.form = ProjectForm(initial=data, instance=data_detail)
		self.context = {
			"page_title":"Detail Data",
			"data_form":self.form,
		}
		return render(self.request, self.template_name, self.context)

	def post(self, *args, **kwargs):
		data_detail = ProjectList.objects.get(id=kwargs['pk'])
		self.form = ProjectForm(self.request.POST,instance=data_detail)
		return redirect('projectList:index')

class UpdateProjectList(UpdateView):
#for detail by id
	Model=ProjectList
	form_class = ProjectForm
	template_name = "ProjectList/update.html"

	def get(self, *args, **kwargs):
		data_update = ProjectList.objects.get(id=kwargs['pk'])
		data = data_update.__dict__
		self.form = ProjectForm(initial=data, instance=data_update)
		self.context = {
			"page_title":"Update Data",
			"data_form":self.form}
		return render(self.request, self.template_name, self.context)
	
	def post(self, *args, **kwargs):
		if kwargs.__contains__('pk'):
			data_update = ProjectList.objects.get(id=kwargs['pk'])
			self.form = ProjectForm(self.request.POST,instance=data_update)
			if self.form.is_valid():
				self.form.save()
				return redirect('projectList:index')	
			return super().form_valid(self.form)