from django.shortcuts import render
from .forms import CartoonImageForm
from .cartoon_conversion import caart

# # Create your views here.

# # def hello (request):
# #   return HttpResponse("Hello World")

# # def cartoon (request):
# #   template = loader.get_template('cartoon.html')
# #   return HttpResponse(template.render())
# #   # return render(request, 'cartoon.html')

def cartoon(request):
    cartoon_result = None
    if request.method == 'POST':
        form = CartoonImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = form.cleaned_data['file_cartoon']
            cartoon_result = caart(image_file)
    print(cartoon_result)  # Check the value in the console
    form = CartoonImageForm()
    return render(request, 'cartoon.html', {'form': form, 'cartoon_result': cartoon_result})