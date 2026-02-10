from django.contrib import admin
from rango.models import Category, Page

# Register your models here.
#chapter 5
from rango.models import Category, Page

#chapter 5 ex
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url")

#chapter 6.1
# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin): prepopulated_fields = {'slug':('name',)}


admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
