from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_something(request):
    return HttpResponse("This is the response")


class HomepageView(TemplateView):
    template_name = 'invoices/home.html'

class signupView(TemplateView):
    template_name = 'invoices/signup.html'

class PricesView(TemplateView):
    template_name = 'invoices/prices.html'
