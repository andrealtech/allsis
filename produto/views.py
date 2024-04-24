from django.shortcuts import render

def cad_produtos(request):
    return render(request, 'cad_produtos.html')


def ver_produtos(request):
    return render(request, 'ver_produtos.html')
