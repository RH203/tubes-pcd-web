from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'home'

# URLConf
urlpatterns = [
  # path('test/', views.hello),
  path('', views.index, name='home_page')
]

# Static
if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)