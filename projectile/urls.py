from calendar import HTMLCalendar
from http.client import HTTPSConnection
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse, HttpResponseForbidden



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),

]
