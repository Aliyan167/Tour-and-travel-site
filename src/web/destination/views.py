from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from .models import Destination
from ..tour.models import Tour
from ..blog.models import BlogPost
from ..website.models import TourFeature,Testimonials


class DestinationView(TemplateView):
    template_name = 'destination.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch all categories dynamically (or use a predefined list)
        categories = Destination.objects.values_list('name', flat=True).distinct()
        context['categories'] = categories

        context['tours'] = Tour.objects.all()

        context['blogs'] = BlogPost.objects.all()[:3]
        context['tour_features'] = TourFeature.objects.all()
        context['testimonials'] = Testimonials.objects.all()[:3]
        # Fetch all destinations
        destinations_list = Destination.objects.all()

        # Apply filters
        selected_categories = self.request.GET.getlist('category')
        if selected_categories:
            destinations_list = destinations_list.filter(name__in=selected_categories)

        # Add pagination
        paginator = Paginator(destinations_list, 1)  # Adjust items per page as needed
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Add the paginated destinations and request to context
        context['destinations'] = page_obj
        context['request'] = self.request  # Pass request for template usage
        return context
