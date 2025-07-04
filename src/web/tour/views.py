from django.views.generic import TemplateView
from .models import Tour, Review
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormView
from .forms import BookingForm


class tourView(TemplateView):
    template_name = 'tour.html'

    def get_context_data(self, **kwargs):
        # Get the base context from the superclass
        context = super().get_context_data(**kwargs)

        # Fetch all tours and order them by 'price' (or any other field you prefer)
        tour_list = Tour.objects.all().order_by('price')

        # Pagination logic: Show 8 tours per page
        paginator = Paginator(tour_list, 8)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Add paginated tours to the context
        context['tours'] = page_obj

        return context


class TourDetailView(TemplateView):
    template_name = 'tour-details.html'

    def get_context_data(self, **kwargs):
        # Get the base context from the superclass
        context = super().get_context_data(**kwargs)

        # Retrieve the specific tour object
        tour_id = self.kwargs.get('pk')  # Assumes you're passing `pk` in the URL
        tour = get_object_or_404(Tour, id=tour_id)
        tour_list = Tour.objects.all().order_by('price')
        context['tours'] = tour_list

        context['tour'] = tour

        # Fetch related reviews
        reviews = Review.objects.filter(tour=tour).order_by('-id')  # Show latest first
        context['reviews'] = reviews

        return context


from .forms import BookingForm
from .models import Booking  # adjust this if you have a Booking model
from .utils import send_reservation_email  # wherever you put your email function


class BookingView(FormView):
    template_name = 'booking.html'
    form_class = BookingForm
    success_url = reverse_lazy('tour:booking')  # Redirect after successful booking

    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.user = self.request.user
        booking.save()

        # Call the email function
        send_reservation_email(
            full_name=booking.full_name,
            recipient_email=booking.email,
            tour_title=booking.tour.title,
            created_at=booking.created_at,
        )

        messages.success(self.request, 'Your booking was successful! Confirmation email sent.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error with your booking. Please try again.')
        return super().form_invalid(form)
