from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# URLConf
urlpatterns = [
  path('test/', views.hello),
  path('index/', views.index)
]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)