# scanner/views.py

from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ScannerImageForm
import os
from .scanner_def import scan_document


file_path = os.path.abspath(os.path.join(settings.BASE_DIR, 'scanner', 'image', 'bahan'))

def scanner(request):
    return render(request, 'scanner/scanner.html')

# def save_image(request):
#     if request.method == 'POST':
#         form = ScannerImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Ambil data dari formulir
#             title = form.cleaned_data['title']
#             image_upload = request.FILES['image_upload']

#             # Tentukan direktori penyimpanan
#             save_directory = os.path.join('scanner', 'image', 'bahan')

#             # Pastikan direktori tersedia, jika tidak, buat direktori
#             os.makedirs(save_directory, exist_ok=True)

#             # Simpan data ke dalam direktori tanpa menyimpan di database
#             # save_path = os.path.join(save_directory, f"{title}.jpg")
#             save_path = os.path.join(save_directory, f"{title}{os.path.splitext(image_upload.name)[1]}")
#             with open(save_path, 'wb+') as destination:
#                 for chunk in image_upload.chunks():
#                     destination.write(chunk)

#             # Redirect atau lakukan hal lain yang sesuai
#             return redirect('scanner:scanner_result')  
#     else:
#         form = ScannerImageForm()

#     return render(request, 'scanner/scanner.html', {'form': form})

def save_image(request):
    if request.method == 'POST':
        form = ScannerImageForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image_upload = request.FILES['image_upload']

            save_directory = os.path.join('scanner', 'image', 'bahan')
            os.makedirs(save_directory, exist_ok=True)

            scanned_results = []
            save_path = os.path.join(save_directory, f"{title}{os.path.splitext(image_upload.name)[1]}")
            with open(save_path, 'wb+') as destination:
                for chunk in image_upload.chunks():
                    destination.write(chunk)

            scanned_path = scan_document(save_path, request)
            scanned_results.append(scanned_path)
            # print(scanned_path)
            # cartoonized_path = (scanned_path, os.path.join(save_directory, f"{title}_scanner.jpg"))

            # return redirect('scanner:scanner_result')
            return render(request, 'scanner/scanner.html', {'form': form, 'scanned_results': scanned_results})

    else:
        form = ScannerImageForm()

    return render(request, 'scanner/scanner.html', {'form': form})

def scanner_reset (request):
    request.session.pop('scanned_result', None)
    return redirect('scanner:scanner_page')
