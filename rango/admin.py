from django.contrib import admin

# Register your models here.
#chapter 5
from rango.models import Category, Page

admin.site.register(Category)
admin.site.register(Page)