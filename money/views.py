from django.shortcuts import render
from django.conf import settings
from .forms import MoneyImageForm
from .uang_matching import uang_matching
import os

# Define the absolute file path
file_path = os.path.abspath(os.path.join(settings.BASE_DIR, 'money', 'image', 'user'))

def money_page(request):
    if request.method == 'POST':
        form = MoneyImageForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image_upload = request.FILES['image_upload']

            # Ensure the directory exists
            save_directory = os.path.join('money', 'image', 'user')
            os.makedirs(save_directory, exist_ok=True)

            # Save the image to the appropriate location
            save_path = os.path.join(save_directory, f"{title}{os.path.splitext(image_upload.name)[1]}")
            with open(save_path, 'wb+') as destination:
                for chunk in image_upload.chunks():
                    destination.write(chunk)

            # Process the image and get the result
            detected_title = uang_matching(save_path)

            return render(request, 'money/money.html', {'detected_title': detected_title})
    else:
        form = MoneyImageForm()

    return render(request, 'money/money.html', {'form': form})
