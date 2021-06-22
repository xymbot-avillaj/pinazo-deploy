from django.contrib import admin
from .models import ProductionTable, Production

# Register your models here.
admin.site.register(Production)
admin.site.register(ProductionTable)