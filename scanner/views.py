# scanner/views.py

from django.shortcuts import render, redirect
from .forms import ScannerImageForm
import os

def scanner(request):
    return render(request, 'scanner.html')

def save_image(request):
    if request.method == 'POST':
        form = ScannerImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Ambil data dari formulir
            title = form.cleaned_data['title']
            image_upload = request.FILES['image_upload']

            # Tentukan direktori penyimpanan
            save_directory = os.path.join('scanner', 'image', 'bahan')

            # Pastikan direktori tersedia, jika tidak, buat direktori
            os.makedirs(save_directory, exist_ok=True)

            # Simpan data ke dalam direktori tanpa menyimpan di database
            # save_path = os.path.join(save_directory, f"{title}.jpg")
            save_path = os.path.join(save_directory, f"{title}{os.path.splitext(image_upload.name)[1]}")
            with open(save_path, 'wb+') as destination:
                for chunk in image_upload.chunks():
                    destination.write(chunk)

            # Redirect atau lakukan hal lain yang sesuai
            return redirect('scanner:scanner_result')  
    else:
        form = ScannerImageForm()

    return render(request, 'scanner.html', {'form': form})
