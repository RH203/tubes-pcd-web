from django.urls import path
from .views import cartoon, save_image, reset_image
from django.conf import settings
from django.conf.urls.static import static
from .views import cartoon, save_image, reset_image


app_name = 'cartoon'

urlpatterns = [
  path('cartoon/', cartoon, name='cartoon_page'),
  path('resultcartoon/', save_image, name='cartoon_result'),
  path('resetcartoon/', reset_image, name='cartoon_reset')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)