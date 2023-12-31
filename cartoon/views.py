from django.shortcuts import render, redirect
from django.conf import settings
from .forms import CartoonImageForm
from .cartoon_def import read_image
import os
# Create your views here.


#file path
file_path = os.path.abspath(os.path.join(settings.BASE_DIR, 'cartoon', 'image', 'bahan'))

def cartoon (request):
  return render(request, 'cartoon/cartoon.html')

def save_image (request):
  if request.method == 'POST':
    form = CartoonImageForm(request.POST, request.FILES)
    if form.is_valid():
            # Ambil data dari formulir
      title = form.cleaned_data['title']
      image_upload = request.FILES['image_upload']

            # Tentukan direktori penyimpanan
      save_directory = os.path.join('cartoon', 'image', 'bahan')

            # Pastikan direktori tersedia, jika tidak, buat direktori
      os.makedirs(save_directory, exist_ok=True)
      cartoon_results = []
      save_path = os.path.join(save_directory, f"{title}{os.path.splitext(image_upload.name)[1]}")
      with open(save_path, 'wb+') as destination:
        for chunk in image_upload.chunks():
          destination.write(chunk)
      
      cartoon_path = read_image(save_path, request)
      cartoon_results.append(cartoon_path)

    return render(request, 'cartoon/cartoon.html', {'form': form, 'cartoon_result': cartoon_results})
  else:
    form = CartoonImageForm()

  return render(request, 'cartoon/cartoon.html', {'form': form})

def reset_image(request):
  request.session.pop('cartoon_result', None)
  return redirect('cartoon:cartoon_page')