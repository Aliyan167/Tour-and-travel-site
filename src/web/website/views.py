from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .models import NewsletterSubscription
from .models import Testimonials, TourFeature
from .models import TourCategory
from ..blog.models import BlogPost
from ..destination.models import Destination
from ..tour.forms import BookingForm
from ..tour.models import Tour


class HomeView(TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        # Call the superclass method to initialize context
        context = super().get_context_data(**kwargs)

        # Add your custom data
        context['testimonials'] = Testimonials.objects.all()[:3]
        context['destinations'] = Destination.objects.all()[:4]

        # Debug the fetched tours
        context['tour_features'] = TourFeature.objects.all()[:10]

        # Debug the TourCategory
        context['tour_categories'] = TourCategory.objects.all()

        tour_list = Tour.objects.all().order_by('price')
        context['tours'] = tour_list

        context['blogs'] = BlogPost.objects.all().order_by('-publication_date')  # Order by latest

        # Fetch the 2 most recent blog posts
        context['recent_posts'] = BlogPost.objects.all().order_by('-publication_date')[:2]

        # Fetch all blog posts and order them by publication date (latest first)
        blog_list = BlogPost.objects.all().order_by('-publication_date')
        context['blogpost'] = blog_list

        return context


class AboutView(TemplateView):
    template_name = 'website/about.html'

    def get_context_data(self, **kwargs):
        # Call the superclass method to initialize context
        context = super().get_context_data(**kwargs)

        # Add your custom data
        context['testimonials'] = Testimonials.objects.all()[:3]
        return context


class ContactView(FormView):
    template_name = 'website/contact.html'  # The template to render
    form_class = BookingForm  # The form to use
    success_message = 'Your booking has been successfully made!'  # Success message after successful submission
    error_message = 'There was an error with your booking. Please try again.'  # Error message for failed submission

    def form_valid(self, form):
        # Save the form data (booking) to the database
        form.save()
        # Send a success message
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        # Handle error on invalid submission
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)

    def get_success_url(self):
        # Redirect to a success page (or home page) after successful submission
        return reverse_lazy('website:home')
