from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.

def count (request):
  # template = loader.get_template('count.html')
  # return HttpResponse(template.render())
  return render(request, 'count.html')
