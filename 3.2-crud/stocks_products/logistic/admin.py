from django.contrib import admin

from .models import Product, StockProduct, Stock


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')


class StockProductInline(admin.TabularInline):
    model = StockProduct


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'address',)

    inlines = (StockProductInline,)
