from django.contrib.auth.models import User
from django.db import models

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=5)  # Рейтинг от 1 до 5
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.user.username}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    composition = models.TextField()
    energy_value = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)
    image = models.ImageField('Изображение товара', upload_to='image/')
    date_added = models.DateTimeField(auto_now_add=True)
    reviews = models.ManyToManyField(Review, related_name='product_reviews', blank=True)

    class Meta:
        ordering = ['pk']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} - {self.price}'