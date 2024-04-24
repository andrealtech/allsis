from django.urls import path

from usuarios.views import home

urlpatterns = [
    path('', home, name='home'),
]
