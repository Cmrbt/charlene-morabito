from django.urls import path
from .views import morabito_home_view, product_catalog_view

urlpatterns = [
    path('', morabito_home_view, name='home'),
    path('pret-a-porter/', product_catalog_view, name='pret-a-porter')

]