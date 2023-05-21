from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from app.models import *

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