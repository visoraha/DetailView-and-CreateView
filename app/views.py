from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *
from django.urls import reverse_lazy

# Create your views here.

class home(TemplateView):
    template_name='app/home.html'
class school_list(ListView):
    #template_name='app/school_list.html'
    model=School
    context_object_name='scl'
class school_detail(DetailView):
    model=School
    #template_name='app/school_detail.html'
    context_object_name='sclobj'

class schoolcreate(CreateView):
    model=School
    fields='__all__'
class schoolupdate(UpdateView):
    model=School
    fields='__all__'
class schooldelete(DeleteView):
    model=School
    context_object_name='schoolobject'
    success_url=reverse_lazy('school_list')


