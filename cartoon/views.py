from django.shortcuts import render, redirect
from django.http import HttpResponseServerError, HttpResponse
from .forms import CartoonImageForm
import cv2
import numpy as np
from django.http import JsonResponse

def cartoon (request):
  return render(request, 'cartoon/cartoon.html')

def image (request):
  if request.method == 'POST':
    form = CartoonImageForm(request.POST, request.FILES)

    if form.is_valid ():
      form.save()
      print("Success")
  else:
    form = CartoonImageForm()
  return render(request, 'cartoon/cartoon.html', {'form': CartoonImageForm()})
