from django.contrib import admin
from .models import Testimonials
from .models import TourFeature
from .models import Contact
from .models import TourCategory
from .models import NewsletterSubscription


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank', 'created_at', 'updated_at')
    search_fields = ('name', 'rank', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(TourFeature)
class TourFeatureAdmin(admin.ModelAdmin):
    list_display = ("location_name", "tours_count")
    search_fields = ("location_name",)
    list_filter = ("tours_count",)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')  # Fields displayed in the admin list view
    search_fields = ('name', 'email', 'phone')  # Enable search by these fields
    list_filter = ('email',)  # Add filtering options
    readonly_fields = ('name', 'email', 'phone', 'message')  # Make fields read-only (optional)


admin.site.register(Contact, ContactAdmin)


@admin.register(TourCategory)
class TourCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'total_tours', 'image_preview')
    search_fields = ('title',)
    readonly_fields = ['image_preview']  # Image preview in the admin panel

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="width: 100px; height: auto;" />'
        return "No Image"

    image_preview.allow_tags = True
    image_preview.short_description = "Image Preview"



@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')  # Display these fields in the admin list view
    search_fields = ('email',)  # Add a search bar for the email field
    list_filter = ('subscribed_at',)  # Add filters for the subscription date
