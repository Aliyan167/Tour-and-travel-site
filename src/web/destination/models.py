from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal


class Destination(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='destination_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0
    )
    duration_days = models.PositiveIntegerField()
    duration_nights = models.PositiveIntegerField()
    best_price_guarantee = models.BooleanField(default=False)
    free_cancellation = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.FloatField(default=0.0)
    total_ratings = models.PositiveIntegerField(null=True, blank=True)

    @property
    def discounted_price(self):
        # Ensure both price and discount are Decimal objects before performing the calculation
        discount_factor = Decimal(1) - self.discount / Decimal(100)
        return self.price * discount_factor

    def __str__(self):
        return self.name
