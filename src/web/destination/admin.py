from django.contrib import admin
from .models import Destination


class DestinationAdmin(admin.ModelAdmin):
    # Fields to display in the list view of the admin panel
    list_display = ('name', 'location', 'price', 'discount', 'duration_days', 'duration_nights', 'best_price_guarantee',
                    'free_cancellation', 'created_at', 'updated_at')

    # Filters to help narrow down the displayed records
    list_filter = ('location', 'best_price_guarantee', 'free_cancellation')

    # Fields to be searchable in the admin panel
    search_fields = ('name', 'location', 'description')

    # Default ordering in the admin list view (by creation date)
    ordering = ('-created_at',)


# Register the Destination model with the admin site
admin.site.register(Destination, DestinationAdmin)
