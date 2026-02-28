from django.urls import path
from mansiapp.views import home

urlpatterns=[
    path('', home, name='home'),
]