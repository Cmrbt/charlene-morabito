from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def morabito_home_view(request):

    return render(request, 'pages/home/morabito.html')

from django.templatetags.static import static

def product_catalog_view(request):
    product_list = [
    ]
    for product in product_list:
        product['image_url'] = static(product['image_path'])

    context = {
        'products': product_list
    }
    return render(request, 'pages/home/catalogue/product_catalog.html', context)


def model_view(request):

    return render(request, 'pages/home/catalogue/model_view.html')