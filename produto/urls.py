from django.urls import path

from produto.views import ver_produtos, cad_produtos

urlpatterns = [
    path('cad_produtos/', cad_produtos, name='cad_produtos'),
    path('ver_produtos/', ver_produtos, name='ver_produtos'),
]
