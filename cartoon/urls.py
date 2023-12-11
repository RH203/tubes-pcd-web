# cartoon/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import cartoon, image

app_name = 'cartoon'

urlpatterns = [
    path('cartoon/', cartoon, name='cartoon_page'),
    path('result/', image, name='cartoon_result')
]

## MEDIA
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    