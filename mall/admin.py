from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Shop)
admin.site.register(ShopRate)
admin.site.register(Product)
admin.site.register(ProductRate)
admin.site.register(Category)
admin.site.register(Template)