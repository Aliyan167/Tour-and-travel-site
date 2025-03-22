from django.contrib import admin
from .models import Testimonials
from .models import TourFeature
from .models import Contact
from .models import TourCategory
from .models import NewsletterSubscription
from .models import Activity
from .models import team


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


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'country', 'city', 'tour')
    list_filter = ('country', 'city', 'tour')
    search_fields = ('full_name', 'email', 'phone_number', 'country', 'city')
    ordering = ('full_name',)
    fieldsets = (
        (None, {
            'fields': ('full_name', 'email', 'phone_number', 'country', 'city', 'state', 'zip_code', 'address')
        }),
        ('Tour Information', {
            'fields': ('tour', 'tour_content')
        }),
    )


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


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


@admin.register(team)
class teamAdmin(admin.ModelAdmin):
    list_display = ('name',  'created_at', 'updated_at')
    search_fields = 'name',
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
