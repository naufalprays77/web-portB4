from django.contrib import admin

# Register your models here.

from .models import Status,Priorty

admin.site.register(Status)
admin.site.register(Priorty)