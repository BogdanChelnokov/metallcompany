# products/models.py

from django.db import models
from django.urls import reverse

class Category(models.Model):
    """Модель категории товаров"""
    name = models.CharField('Название', max_length=100)
    slug = models.SlugField('URL', max_length=100, unique=True)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', upload_to='categories/', blank=True, null=True)
    sort_order = models.IntegerField('Порядок сортировки', default=0)
    is_active = models.BooleanField('Активно', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
    
    class Meta:
        ordering = ['sort_order', 'name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_detail', args=[self.slug])

class Product(models.Model):
    """Модель товара"""
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='products',
        verbose_name='Категория'
    )
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('URL', max_length=200, unique=True)
    description = models.TextField('Описание', blank=True)
    
    # Технические характеристики
    gost = models.CharField('ГОСТ', max_length=50, blank=True)
    steel_grade = models.CharField('Марка стали', max_length=100, blank=True)
    length = models.CharField('Длина', max_length=50, blank=True)
    weight_per_meter = models.DecimalField('Вес п.м (кг)', max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.DecimalField('Цена (руб.)', max_digits=12, decimal_places=2, null=True, blank=True)
    
    # Дополнительно
    image = models.ImageField('Изображение', upload_to='products/', blank=True, null=True)
    is_active = models.BooleanField('Активно', default=True)
    sort_order = models.IntegerField('Порядок сортировки', default=0)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
    
    class Meta:
        ordering = ['sort_order', 'name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    def __str__(self):
        return f"{self.name} ({self.category.name})"
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

class Advantage(models.Model):
    """Модель преимуществ (для блока на главной)"""
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание')
    icon = models.ImageField('Иконка', upload_to='advantages/', blank=True, null=True)
    sort_order = models.IntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активно', default=True)
    
    class Meta:
        ordering = ['sort_order']
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'
    
    def __str__(self):
        return self.title

class SiteSetting(models.Model):
    """Настройки сайта (контакты, заголовки)"""
    key = models.CharField('Ключ', max_length=100, unique=True)
    value = models.TextField('Значение')
    description = models.CharField('Описание', max_length=200, blank=True)
    
    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки сайта'
    
    def __str__(self):
        return self.key