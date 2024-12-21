from django.urls import path
from .views import tourView, TourDetailView, BookingView

app_name = "tour"

urlpatterns = [
    path('', tourView.as_view(), name='tour'),
    path('tour_details/<int:pk>/', TourDetailView.as_view(), name='tour_detail'),
    path('booking/', BookingView.as_view(), name='booking')
]
