from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from modelapp import views


urlpatterns = [
    path('',include('modelapp.urls')),
    path('admin/', admin.site.urls),
    path('paypal/', include("paypal.standard.ipn.urls")),
]+static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)