# products/admin.py

from django.contrib import admin
from .models import Category, Product, Advantage, SiteSetting

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'sort_order', 'is_active', 'created_at']
    list_editable = ['sort_order', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    list_filter = ['is_active']
    fields = ['name', 'slug', 'description', 'image', 'sort_order', 'is_active']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'gost', 'price', 'is_active', 'sort_order']
    list_editable = ['price', 'is_active', 'sort_order']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'gost', 'steel_grade']
    list_filter = ['category', 'is_active']
    fieldsets = (
        ('Основное', {
            'fields': ('category', 'name', 'slug', 'description', 'image')
        }),
        ('Технические характеристики', {
            'fields': ('gost', 'steel_grade', 'length', 'weight_per_meter')
        }),
        ('Цена и сортировка', {
            'fields': ('price', 'sort_order', 'is_active')
        }),
    )

@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ['title', 'sort_order', 'is_active']
    list_editable = ['sort_order', 'is_active']
    search_fields = ['title', 'description']

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['key', 'value', 'description']
    search_fields = ['key', 'value']