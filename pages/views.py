from django.shortcuts import render
from .models import Brand, FirstHomeSection, SecondHomeSection
from django.http import HttpResponse
from django.templatetags.static import static
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def morabito_home_view(request):
    brand = Brand.objects.first()
    if not brand:
        brand = Brand.objects.create()

    first_section = FirstHomeSection.objects.first()
    if not first_section:
        first_section = FirstHomeSection.objects.create()

    second_section = SecondHomeSection.objects.first()
    if not second_section:
        second_section = SecondHomeSection.objects.create()

    context = {
        'brand': brand,
        'first_section': first_section,
        'second_section': second_section,
    }
    return render(request, 'pages/home/morabito.html', context)



def brand_action_handler(request):
    action = request.POST.get('action')

    if action == 'update_brand_info':
        return update_brand_info(request)

    if action == 'update_first_section_info':
        return update_first_section_info(request)
    
    if action == 'reset_first_section':
        return reset_first_section(request)

    return JsonResponse({'status': 'error', 'message': 'Action non reconnue.'})

def reset_first_section(request):
    section_id = request.POST.get('section_id')
    section = get_object_or_404(FirstHomeSection, id=section_id)
    section.delete()
    return JsonResponse({'status': 'success', 'message': 'Première section supprimée.'})


def update_first_section_info(request):
    section_id = request.POST.get('section_id')
    section = get_object_or_404(FirstHomeSection, id=section_id)

    section.title = request.POST.get('title', section.title)
    section.description = request.POST.get('description', section.description)
    section.link_text = request.POST.get('link_text', section.link_text)
    section.link_url = request.POST.get('link_url', section.link_url)

    if 'image' in request.FILES:
        print("IMAGE REÇUE :", request.FILES['image'])
        section.image = request.FILES['image']
    else:
        print("AUCUNE IMAGE REÇUE")

    section.save()

    return JsonResponse({'status': 'success', 'message': 'Première section mise à jour.'})


def update_brand_info(request):
    brand_id = request.POST.get('brand_id')
    brand = get_object_or_404(Brand, id=brand_id)

    brand.name = request.POST.get('name', brand.name)
    brand.slogan = request.POST.get('slogan', brand.slogan)
    brand.call_to_action = request.POST.get('call_to_action', brand.call_to_action)

    brand.save()

    return JsonResponse({'status': 'success', 'message': 'Marque mise à jour avec succès.'})


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



def cart_view(request):

    return render(request, 'pages/home/catalogue/cart_view.html')