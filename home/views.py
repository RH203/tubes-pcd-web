from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
# Create your views here.

# def hello (request):
#   return HttpResponse("Hello World")

def index (request):
  # template = loader.get_template('index.html')
  # return HttpResponse(template.render())
  return render(request, 'index.html')