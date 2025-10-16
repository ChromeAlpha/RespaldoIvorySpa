from django.contrib import admin
from .models import Project
from products.models import Product

admin.site.site_header = "IvorySpa-Shop Administración"
admin.site.site_title = "IvorySpa-Shop Portal Admin"
admin.site.index_title = "Bienvenido al Panel de Administración de IvorySpa-Shop"
