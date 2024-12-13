from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'second_task/class_template.html'



# Create your views here.
def index(request):
    return render(request, 'second_task/func_template.html')

