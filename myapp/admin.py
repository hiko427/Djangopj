from django.contrib import admin
from .models import Product
# Register your models here.
admin.site.register(Product)
admin.site.site_header = "Buy & Sell Website"
admin.site.site_title = "ABC Buying"
