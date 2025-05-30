from django.db import models
from src.web.tour.models import TourCategory
class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='testimonials_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TourFeature(models.Model):
    location_name = models.CharField(max_length=255, verbose_name="Location Name")
    image = models.ImageField(upload_to="features/", verbose_name="Feature Image")
    tours_count = models.PositiveIntegerField(default=0, verbose_name="Number of Tours")

    class Meta:
        verbose_name = "Tour Feature"
        verbose_name_plural = "Tour Features"

    def __str__(self):
        return self.location_name


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    tour = models.ForeignKey(TourCategory, on_delete=models.CASCADE, related_name="contact_tours")  # Changed related_name
    tour_content = models.TextField()

    def __str__(self):
        return f"{self.full_name} - {self.email}"


class TourCategory(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tour_categories/')
    total_tours = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Tour Category"
        verbose_name_plural = "Tour Category"

    def __str__(self):
        return self.title


class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Activity(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='activities/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class team(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
