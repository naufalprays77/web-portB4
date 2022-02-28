from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from AppGeneral.models import *
from AppTaskList.forms import TaskForm
from .models import ProjectList, TaskList
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView, 
    DeleteView
)

class TaskProject(ListView):
    model = TaskList
    template_name = 'TaskList/index.html'
    context_object_name = 'taskList'
    ordering = ['strProjectName']
    

    
class CreateTaskList(CreateView):
    Model=TaskList
    form_class = TaskForm
    template_name = 'TaskList/create.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['strStatus'] = Status.objects.all()
        context['strPriorty'] = Priorty.objects.all()
        context['strProjectName'] = ProjectList.objects.all()
        return context
    
    def post(self, request):
        if request.method == 'POST':
            self.form = TaskForm(self.request.POST)
            b = TaskForm(self.request.POST)
            print(b)
            if self.form.is_valid():
                self.form.save()
                return redirect('taskList:index')
            return super().form_valid(self.form)

class DeleteTasktList(DeleteView):
	model = TaskList
	template_name = 'TaskList/confirm_delete.html'
	success_url = reverse_lazy('taskList:index')

class DetailTaskList(DetailView):
#for detail by id
	Model=TaskList
	form_class = TaskForm
	template_name = "TaskList/detail.html"

	def get(self, *args, **kwargs):
		data_detail = TaskList.objects.get(id=kwargs['pk'])
		data = data_detail.__dict__
		self.form = TaskForm(initial=data, instance=data_detail)
		self.context = {
			"page_title":"Detail Data",
			"data_form":self.form,
		}
		return render(self.request, self.template_name, self.context)

	def post(self, *args, **kwargs):
		data_detail = TaskList.objects.get(id=kwargs['pk'])
		self.form = TaskForm(self.request.POST,instance=data_detail)
		return redirect('taskList:index')

class UpdateTaskList(UpdateView):
#for detail by id
	Model=TaskList
	form_class = TaskForm
	template_name = "TaskList/update.html"

	def get(self, *args, **kwargs):
		data_update = TaskList.objects.get(id=kwargs['pk'])
		data = data_update.__dict__
		self.form = TaskForm(initial=data, instance=data_update)
		self.context = {
			"page_title":"Update Data",
			"data_form":self.form,
		}
		return render(self.request, self.template_name, self.context)
	
	def post(self, *args, **kwargs):
		if kwargs.__contains__('pk'):
			data_update = TaskList.objects.get(id=kwargs['pk'])
			self.form = TaskForm(self.request.POST,instance=data_update)
			if self.form.is_valid():
				self.form.save()
				return redirect('taskList:index')	
			return super().form_valid(self.form)