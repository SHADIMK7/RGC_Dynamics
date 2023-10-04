from django.contrib import admin
from django.urls import path

from api_app import views

urlpatterns = [
    path('employeedetails',views.simple_details,name='simple_details'),
    path('employeedetails/<int:id>',views.employeedetails,name='employeedetails')
]
