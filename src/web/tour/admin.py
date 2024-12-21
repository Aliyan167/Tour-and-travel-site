from django.utils.html import mark_safe
from django.contrib import admin
from .models import Tour, TourCategory, Review, Booking


@admin.register(TourCategory)
class TourCategoryAdmin(admin.ModelAdmin):
    """Admin configuration for TourCategory."""
    list_display = ('id', 'name')  # Display category ID and name
    search_fields = ('name',)  # Enable search by name
    ordering = ('name',)  # Sort categories by name


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    """Admin configuration for Tour."""
    list_display = (
        'title', 'category', 'destination', 'price', 'duration_days',
        'image_preview', 'rating', 'total_ratings_display'
    )  # Fields displayed in list view
    search_fields = ('title', 'destination', 'category__name')  # Search by title, destination, category
    list_filter = ('category',)  # Filter by category
    readonly_fields = ('image_preview', 'total_ratings_display',)  # Make specific fields read-only in the form

    def image_preview(self, obj):
        """Preview tour image in admin list and form."""
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" style="border-radius: 5px;" />')
        return "No Image"

    image_preview.short_description = 'Image Preview'

    def total_ratings_display(self, obj):
        """Display the total number of reviews for a tour."""
        return obj.reviews.count()

    total_ratings_display.short_description = 'Total Ratings'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin configuration for Review."""
    list_display = ('user', 'tour', 'star_rating')  # Display user, tour, and star rating
    search_fields = ('user__username', 'tour__title')  # Enable search by username and tour title
    list_filter = ('star_rating',)  # Filter by star rating


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'tour', 'created_at')
    list_filter = ('country', 'state', 'city', 'created_at', 'tour')
    search_fields = ('full_name', 'email', 'phone_number', 'tour__name')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    fieldsets = (
        ("Personal Information", {
            'fields': ('full_name', 'email', 'phone_number')
        }),
        ("Address Details", {
            'fields': ('country', 'state', 'city', 'zip_code', 'address_2')
        }),
        ("Tour Details", {
            'fields': ('tour', 'tour_content')
        }),
        ("Timestamps", {
            'fields': ('created_at',)
        }),
    )