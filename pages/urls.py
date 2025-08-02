from django.urls import path
from .views import morabito_home_view, product_catalog_view, model_view, cart_view, brand_action_handler, model_view2, toggle_display_status, toggle_product_catalog_visibility, delete_product

urlpatterns = [
    path('', morabito_home_view, name='home'),
    path('pret-a-porter/', product_catalog_view, name='pret-a-porter'),
    path('model/', model_view, name='model'),
    path('cart/', cart_view, name='cart'),
    path('brand/action/', brand_action_handler, name='brand_action_handler'),
    path('model2/<int:product_id>/', model_view2, name='model2'),
    path('toggle-display/', toggle_display_status, name='toggle_display_status'),
    path('products/<int:product_id>/toggle-visibility/', toggle_product_catalog_visibility, name='toggle_product_catalog_visibility'),
    path('products/<int:product_id>/delete/', delete_product, name='delete_product'),

]