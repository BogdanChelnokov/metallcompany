# products/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Category, Product, Advantage, SiteSetting

def get_site_settings():
    """Получает настройки сайта в виде словаря"""
    settings = {}
    try:
        for setting in SiteSetting.objects.all():
            settings[setting.key] = setting.value
    except:
        pass
    return settings

def home(request):
    """Главная страница"""
    categories = Category.objects.filter(is_active=True)
    advantages = Advantage.objects.filter(is_active=True)
    site_settings = get_site_settings()
    
    context = {
        'categories': categories,
        'advantages': advantages,
        'site_settings': site_settings,
    }
    return render(request, 'main/index.html', context)

def category_content(request, slug):
    """
    API-эндпоинт для загрузки контента категории через AJAX
    Возвращает HTML с описанием и товарами
    """
    category = get_object_or_404(Category, slug=slug, is_active=True)
    products = category.products.filter(is_active=True)
    
    # Рендерим HTML-блок
    html = render_to_string('main/_category_content.html', {
        'category': category,
        'products': products,
    })
    
    return JsonResponse({'html': html})

# Старые вьюхи для страниц (можно оставить для SEO)
def category_detail(request, slug):
    """Страница категории (для SEO и прямых ссылок)"""
    category = get_object_or_404(Category, slug=slug, is_active=True)
    products = category.products.filter(is_active=True)
    site_settings = get_site_settings()
    
    context = {
        'category': category,
        'products': products,
        'site_settings': site_settings,
    }
    return render(request, 'main/category_detail.html', context)

def product_detail(request, category_slug, product_slug):
    """Страница товара"""
    product = get_object_or_404(
        Product, 
        slug=product_slug, 
        category__slug=category_slug,
        is_active=True
    )
    site_settings = get_site_settings()
    
    context = {
        'product': product,
        'site_settings': site_settings,
    }
    return render(request, 'main/product_detail.html', context)