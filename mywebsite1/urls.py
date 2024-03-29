from django.contrib import admin
from django.urls import path,include
from .views import homePage

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homePage),
    path('voting/', include('votingapp.urls')),
    path('employee/', include('employee.urls'), name="Employee"),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
