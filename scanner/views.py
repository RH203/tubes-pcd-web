from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
def scanner (request):
  return render(request, 'scanner.html')
  # template = loader.get_template('scanner.html')
  # return HttpResponse(template.render())