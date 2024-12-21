from django.db import models
from django.conf import settings
from tinymce.models import HTMLField


class TourCategory(models.Model):
    """Model for categories like 'snorkeling', 'adventure', etc."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tour(models.Model):
    """Model for storing details about a tour."""
    title = models.CharField(max_length=255)
    description = models.TextField(default='No description available')
    category = models.ForeignKey(TourCategory, on_delete=models.CASCADE, related_name="tours")
    destination = models.CharField(max_length=200)  # Example: "Paris, France"
    image = models.ImageField(upload_to="tour_images/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.PositiveIntegerField()
    rating = models.FloatField(default=0.0)  # The average rating (e.g., 4.8)
    total_ratings = models.PositiveIntegerField(null=True, blank=True)  # Total number of ratings (e.g., 269)
    content = HTMLField(default='No content available')
    image1 = models.ImageField(upload_to="tour_images/", null=True, blank=True)
    image2 = models.ImageField(upload_to="tour_images/", null=True, blank=True)
    image3 = models.ImageField(upload_to="tour_images/", null=True, blank=True)
    image4 = models.ImageField(upload_to="tour_images/", null=True, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    """Model for storing star ratings (user's review with stars)."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="reviews")
    star_rating = models.PositiveSmallIntegerField()  # Stars out of 5

    def __str__(self):
        return f"{self.user.username} - {self.tour.title} - {self.star_rating} Stars"


class Booking(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    # ForeignKey to dynamically fetch tours from the database
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    tour_content = models.TextField()

    # Timestamp fields
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.tour.title}"
