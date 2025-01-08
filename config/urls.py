from django.contrib import admin
from django.urls import path
from controller import indexController
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.http import require_http_methods

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexController.index, name='index'),

]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
