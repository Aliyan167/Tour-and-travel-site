from django.urls import path

from .views import (
    HomeView, AboutView, ContactView, ActivityView
)

app_name = "website"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('activities/', ActivityView.as_view(), name='activities')

]
