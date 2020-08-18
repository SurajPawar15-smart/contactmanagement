
from django.contrib import admin
from django.urls import path, include
from . import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', include('Contacts.urls'), name='contacts'),
    path('', views.home_page, name='home'),
]
