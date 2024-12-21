from django.urls import path
from .views import DestinationView

app_name = "destination"

urlpatterns = [
    path('', DestinationView.as_view(), name='destination'),
]


