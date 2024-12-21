from django.shortcuts import render
from django.views.generic import TemplateView
from .models import BlogPost
from django.core.paginator import Paginator


class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch all blog posts
        context['blogs'] = BlogPost.objects.all().order_by('-publication_date')  # Order by latest

        # Fetch the 2 most recent blog posts
        context['recent_posts'] = BlogPost.objects.all().order_by('-publication_date')[:2]

        # Fetch all blog posts and order them by publication date (latest first)
        blog_list = BlogPost.objects.all().order_by('-publication_date')

        # Pagination logic
        paginator = Paginator(blog_list, 3)  # Show 3 posts per page
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['blogs'] = page_obj
        context['recent_posts'] = BlogPost.objects.all().order_by('-publication_date')[:2]

        return context


class BlogDetailView(TemplateView):
    template_name = 'blog-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_id = kwargs.get('pk')  # Get primary key from URL
        context['blog'] = BlogPost.objects.get(pk=blog_id)  # Fetch the Blog object
        return context
