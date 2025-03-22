from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .models import Testimonials, TourFeature, Activity, team
from .models import TourCategory
from ..blog.models import BlogPost
from ..destination.models import Destination
from ..tour.forms import BookingForm
from ..tour.models import Tour
from .forms import ContactForm, NewsletterSubscriptionForm


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
        context['newsletter_form'] = NewsletterSubscriptionForm()

        return context

    def post(self, request, *args, **kwargs):
        # Handle form submission
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()  # Save the email to the database
            messages.success(request, 'Thank you for subscribing to our newsletter!')
            return redirect('website:home')
        else:
            messages.error(request, 'Please enter a valid email address.')

        # After form submission, re-render the page with updated context
        return self.get(request, *args, **kwargs)


class AboutView(TemplateView):
    template_name = 'website/about.html'

    def get_context_data(self, **kwargs):
        # Call the superclass method to initialize context
        context = super().get_context_data(**kwargs)

        # Add your custom data
        context['testimonials'] = Testimonials.objects.all()[:3]
        context['teams'] = team.objects.all()
        context['newsletter_form'] = NewsletterSubscriptionForm()
        return context


def post(self, request, *args, **kwargs):
    # Handle form submission
    form = NewsletterSubscriptionForm(request.POST)
    if form.is_valid():
        form.save()  # Save the email to the database
        messages.success(request, 'Thank you for subscribing to our newsletter!')
        return redirect('website:home')
    else:
        messages.error(request, 'Please enter a valid email address.')

    # After form submission, re-render the page with updated context
    return self.get(request, *args, **kwargs)


class ContactView(FormView):
    template_name = 'website/contact.html'  # The template to render
    form_class = ContactForm  # The form to use
    success_message = 'Your message has been successfully sent!'  # Success message after successful submission
    error_message = 'There was an error sending your message. Please try again.'  # Error message for failed submission
    success_url = reverse_lazy('website:home')  # Redirect to this URL after success

    def form_valid(self, form):
        # Save the form data (contact) to the database
        form.save()
        # Send a success message
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        # Handle error on invalid submission
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)


class ActivityView(TemplateView):
    template_name = 'website/activities.html'

    def get_context_data(self, **kwargs):
        # Get the default context data
        context = super().get_context_data(**kwargs)
        # Add the activities to the context
        context['activities'] = Activity.objects.all()
        context['newsletter_form'] = NewsletterSubscriptionForm()
        return context

    def post(self, request, *args, **kwargs):
        # Handle form submission
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()  # Save the email to the database
            messages.success(request, 'Thank you for subscribing to our newsletter!')
            return redirect('website:home')
        else:
            messages.error(request, 'Please enter a valid email address.')

        # After form submission, re-render the page with updated context
        return self.get(request, *args, **kwargs)
