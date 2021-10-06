from django.shortcuts import render
from django.views.generic import View , TemplateView , DetailView , ListView
from django.http import HttpResponse
from basic_app.models import Student , School

from cbv_project.settings import TEMPLATE_DIR

class IndexView(TemplateView):
    template_name = "basic_app/index.html"


class SchoolListView(ListView):
    model = School
    context_object_name = "school_list"

class SchoolDetailView(DetailView):
    model = School
    template_name = "basic_app/school_detail.html"
    context_object_name ="school_detail"

    

# Create your views here.
