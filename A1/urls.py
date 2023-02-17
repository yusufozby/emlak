from django.contrib import admin
from django.urls import path
from myApp.views import *
from django.conf import settings
from django.conf.urls.static import static
from A1.settings import MEDIA_URL,MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('detail/<title>/',detail,name="detail"),
] + static (settings.MEDIA_URL,document_root = MEDIA_ROOT)
