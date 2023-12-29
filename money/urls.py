from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import money_page

app_name = 'money'

# URLConf
urlpatterns = [
  path('money/', money_page, name='money_page')
  # path('resetmoney/', money_reset, name='money_reset')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)