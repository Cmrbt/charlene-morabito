from django.shortcuts import render
from .models import ( 
        Brand, FirstHomeSection, SecondHomeSection, 
        ReadyToWearSection, LookbookSection, LookbookImage, 
        HeritageIntro, HeritageBlockOne, HeritageBlockThree, 
        HeritageBlockTwo, Product , ProductImage
    )
from django.http import HttpResponse
from django.templatetags.static import static
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils.text import slugify


def morabito_home_view(request):
    brand = Brand.objects.first() or Brand.objects.create()
    first_section = FirstHomeSection.objects.first() or FirstHomeSection.objects.create()
    second_section = SecondHomeSection.objects.first() or SecondHomeSection.objects.create()
    ready_section = ReadyToWearSection.objects.first() or ReadyToWearSection.objects.create()
    lookbook_section = LookbookSection.objects.first() or LookbookSection.objects.create()
    heritage_intro = HeritageIntro.objects.first() or HeritageIntro.objects.create()
    block_one = HeritageBlockOne.objects.first() or HeritageBlockOne.objects.create()
    block_two = HeritageBlockTwo.objects.first() or HeritageBlockTwo.objects.create()
    block_three = HeritageBlockThree.objects.first() or HeritageBlockThree.objects.create()

    lookbook_images = lookbook_section.images.all()

    context = {
        'brand': brand,
        'first_section': first_section,
        'second_section': second_section,
        'ready_section': ready_section,
        'lookbook_section': lookbook_section,
        'lookbook_images': lookbook_images,
        'heritage_intro': heritage_intro,
        'heritage_block_one': block_one,
        'heritage_block_two': block_two,
        'heritage_block_three': block_three,
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

    if action == 'update_second_section_info':
        return update_second_section_info(request)

    if action == 'reset_second_section':
        return reset_second_section(request)

    if action == 'update_ready_section_info':
        return update_ready_section_info(request)

    if action == 'reset_ready_section':
        return reset_ready_section(request)

    if action == 'update_lookbook_section_info':
        return update_lookbook_section_info(request)

    if action == 'reset_lookbook_section':
        return reset_lookbook_section(request)

    if action == 'delete_lookbook_image':
        return delete_lookbook_image(request)

    if action == 'update_heritage_intro_info':
        return update_heritage_intro_info(request)
    
    if action == 'reset_heritage_intro':
        return reset_heritage_intro(request)

    if action == 'update_heritage_block_one_info':
        return update_heritage_block_one_info(request)
      
    if action == 'reset_heritage_block_one':
        return reset_heritage_block_one(request)
    

    if action == 'update_heritage_block_two_info':
        return update_heritage_block_two_info(request)

    if action == 'reset_heritage_block_two':
        return reset_heritage_block_two(request)

    if action == 'update_heritage_block_three_info':
        return update_heritage_block_three_info(request)

    if action == 'reset_heritage_block_three':
        return reset_heritage_block_three(request)

    if action == 'update_brand_contact_info':
        return update_brand_contact_info(request)

    if action == 'create_product_title':
        return create_product_title(request)

    if action == 'update_product_images':
        return update_product_images(request)

    if action == 'delete_product_image':
        return delete_product_image(request)


    return JsonResponse({'status': 'error', 'message': 'Action non reconnue.'})


def update_product_images(request):
    product_id = request.POST.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    print(f"Produit ciblé : {product.name} (ID: {product.id})")

    if 'main_image' in request.FILES:
        product.main_image = request.FILES['main_image']
        product.save()
        print(f"Image principale enregistrée : {product.main_image.name}")

    extra_images = request.FILES.getlist('extra_images')
    if extra_images:
        for img in extra_images:
            ProductImage.objects.create(product=product, image=img)
            print(f"Image associée ajoutée : {img.name}")

    return JsonResponse({'status': 'success'})


def delete_product_image(request):
    image_id = request.POST.get('image_id')
    image = get_object_or_404(ProductImage, id=image_id)
    image.image.delete(save=False)
    image.delete()
    return JsonResponse({'status': 'success'})




def create_product_title(request):
    name = request.POST.get('name')
    if not name:
        return JsonResponse({'status': 'error', 'message': 'Nom requis.'})

    product = Product.objects.create(name=name, slug=slugify(name), price=0)
    return JsonResponse({'status': 'success', 'message': 'Produit créé.', 'product_id': product.id})



def update_brand_contact_info(request):
    brand = Brand.objects.first()
    if not brand:
        brand = Brand.objects.create()

    brand.email = request.POST.get('email', brand.email)
    brand.phone = request.POST.get('phone', brand.phone)
    brand.save()

    return JsonResponse({'status': 'success', 'message': 'Coordonnées mises à jour.'})



def update_heritage_block_three_info(request):
    section_id = request.POST.get('section_id')
    section = get_object_or_404(HeritageBlockThree, id=section_id)

    section.title = request.POST.get('title', section.title)
    section.description = request.POST.get('description', section.description)

    if 'image' in request.FILES:
        section.image = request.FILES['image']

    section.save()
    return JsonResponse({'status': 'success', 'message': 'Bloc patrimoine 3 mis à jour.'})


def reset_heritage_block_three(request):
    section_id = request.POST.get('section_id')
    section = get_object_or_404(HeritageBlockThree, id=section_id)

    section.title = ''
    section.description = ''
    section.image.delete(save=False)
    section.image = None

    section.save()
    return JsonResponse({'status': 'success', 'message': 'Bloc patrimoine 3 réinitialisé.'})



def update_heritage_block_two_info(request):
    section_id = request.POST.get('section_id')
    section = get_object_or_404(HeritageBlockTwo, id=section_id)

    section.title = request.POST.get('title', section.title)
    section.description = request.POST.get('description', section.description)

    if 'image' in request.FILES:
        section.image = request.FILES['image']

    section.save()
    return JsonResponse({'status': 'success', 'message': 'Bloc patrimoine 2 mis à jour.'})


def reset_heritage_block_two(request):
    section_id = request.POST.get('section_id')
    section = get_object_or_404(HeritageBlockTwo, id=section_id)

    section.title = ''
    section.description = ''
    section.image.delete(save=False)
    section.image = None

    section.save()
    return JsonResponse({'status': 'success', 'message': 'Bloc patrimoine 2 réinitialisé.'})


def update_heritage_block_one_info(request):
    section_id = request.POST.get('section_id')
    section = get_object_or_404(HeritageBlockOne, id=section_id)

    section.title = request.POST.get('title', section.title)
    section.description = request.POST.get('description', section.description)

    if 'image' in request.FILES:
        section.image = request.FILES['image']

    section.save()
    return JsonResponse({'status': 'success', 'message': 'Bloc patrimoine 1 mis à jour.'})


def reset_heritage_block_one(request):
    section_id = request.POST.get('section_id')
    section = get_object_or_404(HeritageBlockOne, id=section_id)

    section.title = ''
    section.description = ''
    section.image.delete(save=False)
    section.image = None

    section.save()
    return JsonResponse({'status': 'success', 'message': 'Bloc patrimoine 1 réinitialisé.'})



def update_heritage_intro_info(request):
    section_id = request.POST.get('section_id')
    section = get_object_or_404(HeritageIntro, id=section_id)

    section.title = request.POST.get('title', section.title)
    section.description = request.POST.get('description', section.description)
    section.save()

    return JsonResponse({'status': 'success', 'message': 'Intro mise à jour.'})

def reset_heritage_intro(request):
    section_id = request.POST.get('section_id')
    section = get_object_or_404(HeritageIntro, id=section_id)

    section.title = ''
    section.description = ''
    section.save()

    return JsonResponse({'status': 'success', 'message': 'Intro réinitialisée.'})

def update_lookbook_section_info(request):
    section_id = request.POST.get('section_id')
    section = get_object_or_404(LookbookSection, id=section_id)

    section.subtitle = request.POST.get('subtitle', section.subtitle)
    section.save()

    if request.FILES.getlist('images'):
        for img in request.FILES.getlist('images'):
            LookbookImage.objects.create(section=section, image=img)

    return JsonResponse({'status': 'success', 'message': 'Section lookbook mise à jour.'})


def reset_lookbook_section(request):
    section_id = request.POST.get('section_id')
    section = get_object_or_404(LookbookSection, id=section_id)

    LookbookImage.objects.filter(section=section).delete()
    section.subtitle = ''
    section.save()

    return JsonResponse({'status': 'success', 'message': 'Section lookbook réinitialisée.'})


def delete_lookbook_image(request):
    image_id = request.POST.get('image_id')
    try:
        image = LookbookImage.objects.get(id=image_id)
        image.delete()
        return JsonResponse({'status': 'success', 'message': 'Image supprimée.'})
    except LookbookImage.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Image introuvable.'})


def update_ready_section_info(request):
    section_id = request.POST.get('section_id')
    section = get_object_or_404(ReadyToWearSection, id=section_id)

    section.subtitle = request.POST.get('subtitle', section.subtitle)
    section.title = request.POST.get('title', section.title)
    section.link_text = request.POST.get('link_text', section.link_text)
    section.link_url = request.POST.get('link_url', section.link_url)

    if 'background' in request.FILES:
        print("IMAGE PRÊT-A-PORTER REÇUE :", request.FILES['background'])
        section.background = request.FILES['background']
    else:
        print("AUCUNE IMAGE PRÊT-A-PORTER REÇUE")

    section.save()
    return JsonResponse({'status': 'success', 'message': 'Section prêt-à-porter mise à jour.'})


def reset_ready_section(request):
    section_id = request.POST.get('section_id')
    section = get_object_or_404(ReadyToWearSection, id=section_id)
    section.delete()
    return JsonResponse({'status': 'success', 'message': 'Section prêt-à-porter supprimée.'})




def update_second_section_info(request):
    section_id = request.POST.get('section_id')
    section = get_object_or_404(SecondHomeSection, id=section_id)

    section.title = request.POST.get('title', section.title)
    section.description = request.POST.get('description', section.description)
    section.link_text = request.POST.get('link_text', section.link_text)
    section.link_url = request.POST.get('link_url', section.link_url)

    if 'image' in request.FILES:
        print("IMAGE 2 REÇUE :", request.FILES['image'])
        section.image = request.FILES['image']
    else:
        print("AUCUNE IMAGE 2 REÇUE")

    section.save()
    return JsonResponse({'status': 'success', 'message': 'Deuxième section mise à jour.'})


def reset_second_section(request):
    section_id = request.POST.get('section_id')
    section = get_object_or_404(SecondHomeSection, id=section_id)
    section.delete()
    return JsonResponse({'status': 'success', 'message': 'Deuxième section supprimée.'})




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



def cart_view(request):

    return render(request, 'pages/home/catalogue/cart_view.html')


def model_view(request):

    return render(request, 'pages/home/catalogue/model_view.html')



def model_view2(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    context = {
        'product': product
    }
    return render(request, 'pages/home/catalogue/model_view2.html', context)
