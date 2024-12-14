from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Main(TemplateView):
    template_name = 'third_task/main_page_template.html'


class Shop(TemplateView):
    template_name = 'third_task/shop_template.html'


class Basket(TemplateView):
    template_name = 'third_task/basket_template.html'
