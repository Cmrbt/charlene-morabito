from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def morabito_home_view(request):

    return render(request, 'pages/home/morabito.html')

from django.templatetags.static import static

def product_catalog_view(request):
    # This data will come from your database later
    product_list = [
        {
            "name": "Robe ample ceinturée",
            "price": "3,100.00",
            "image_path": "pages/images/products/robe1.jpg"
        },
        {
            "name": "Robe courte inspiration Polo",
            "price": "2,000.00",
            "image_path": "pages/images/products/robe2.jpg"
        },
        {
            "name": "Jupe",
            "price": "2,100.00",
            "image_path": "pages/images/products/jupe1.jpg"
        },
        {
            "name": "Robe en maille",
            "price": "2,550.00",
            "image_path": "pages/images/products/robe3.jpg"
        },
        {
            "name": "Ensemble chemise et short",
            "price": "2,800.00",
            "image_path": "pages/images/products/ensemble1.jpg"
        },
        {
            "name": "Veste courte",
            "price": "3,500.00",
            "image_path": "pages/images/products/veste1.jpg"
        },
    ]

    # Process static paths for the template
    for product in product_list:
        product['image_url'] = static(product['image_path'])

    context = {
        'products': product_list
    }


    return render(request, 'pages/home/catalogue/product_catalog.html', context)