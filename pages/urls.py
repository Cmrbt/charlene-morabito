from django.urls import path
from .views import morabito_home_view, product_catalog_view, model_view, cart_view, brand_action_handler

urlpatterns = [
    path('', morabito_home_view, name='home'),
    path('pret-a-porter/', product_catalog_view, name='pret-a-porter'),
    path('model/', model_view, name='model'),
    path('cart/', cart_view, name='cart'),
    path('brand/action/', brand_action_handler, name='brand_action_handler'),
]