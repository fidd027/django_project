
from django.urls import path
from store.views import index, about, products_json, products, product_detail

app_name = 'store'

urlpatterns = [
    path('', index, name='home'),
    path('about/',about, name='about'),
    path('products.json/', products_json, name='products_json'),
    path('products/', products, name='products'),
    path('products/<int:product_pk>/',product_detail, name = 'product_detail'),

]