from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import cartoon

app_name = 'cartoon'

# URLConf
urlpatterns = [
  path('cartoon/', views.cartoon, name='cartoon_page'),
  path('cartoon/result', cartoon, name='cartoon_result')
]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)