from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
# Create your views here.

# def hello (request):
#   return HttpResponse("Hello World")

def cartoon (request):
  template = loader.get_template('cartoon.html')
  return HttpResponse(template.render())
  # return render(request, 'cartoon.html')