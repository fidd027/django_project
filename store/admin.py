from django.contrib import admin

from store.models import Product
from store.models import Category, Product

admin.site.register([Category, Product])


