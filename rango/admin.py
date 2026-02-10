from django.contrib import admin

# Register your models here.
#chapter 5
from rango.models import Category, Page

#chapter 5 ex
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url")

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
