from django.contrib import admin
from django.urls import path
from mainapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rec/', rec)
]
