from django.contrib import admin
from .models import Category, Product, ProductImage, Contact
# Register your models here.

class ProductImageAdmin(admin.TabularInline): 
	model = ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug'] 
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
	list_filter = ['available', 'created', 'updated'] 
	list_editable = ['price', 'available'] 
	prepopulated_fields = {'slug': ('name',)}
	inlines = [ProductImageAdmin]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ['name', 'email'] 

