from django.db import models


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
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


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