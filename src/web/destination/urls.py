from django.urls import path
from .views import DestinationView, DestinationDetailView

app_name = "destination"

urlpatterns = [
    path('', DestinationView.as_view(), name='destination'),
    path('destination-detail/<int:pk>/', DestinationDetailView.as_view(), name='destination-detail')
]
