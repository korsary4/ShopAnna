from django.contrib import admin

from shop.models import Product, Review

class ReviewInline(admin.TabularInline):
    model = Product.reviews.through
    extra = 0  # Количество пустых форм для создания отзывов


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'date_added',)
    list_filter = ('user', 'rating', 'date_added',)
    search_fields = ('user__username', 'comment',)
    list_per_page = 20

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date_added',)
    list_filter = ('name', 'date_added',)
    search_fields = ('name', 'description',)
    list_per_page = 20
    inlines = [ReviewInline]




