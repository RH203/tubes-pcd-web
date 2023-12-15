from django.urls import path
from .views import scanner, save_image, scanner_reset
from django.conf import settings
from django.conf.urls.static import static

app_name = 'scanner'

# URLConf
urlpatterns = [
  path('scanner/', scanner, name='scanner_page'),
  path('result/', save_image, name="scanner_result"),
  path('reset/', scanner_reset, name="scanner_reset")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)