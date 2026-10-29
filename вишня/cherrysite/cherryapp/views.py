from django.shortcuts import render

def main_func(request):
    return render(request, template_name='main.html')


def info_func(request):
    return render(request, template_name='info.html')


def products_func(request):
    return render(request, template_name='products.html')


def cart_func(request):
    return render(request, template_name='cart.html')