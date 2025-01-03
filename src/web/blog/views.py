from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, FormView
from .models import BlogPost, Comment
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import CommentForm


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


class BlogDetailView(FormView):
    template_name = 'blog-details.html'
    form_class = CommentForm  # The form to use

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_id = self.kwargs.get('pk')  # Get the blog post ID from the URL
        blog = get_object_or_404(BlogPost, pk=blog_id)
        context['blog'] = blog
        context['comments'] = blog.comments.all()  # Use the related_name to fetch comments
        return context

    def form_valid(self, form):
        # Associate the comment with the blog post and save
        blog_id = self.kwargs.get('pk')  # Get the blog post ID from the URL
        blog = get_object_or_404(BlogPost, pk=blog_id)

        comment = form.save(commit=False)
        comment.blog = blog  # Link the comment to the blog post
        comment.save()

        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        # Add error message for invalid form submissions
        messages.error(self.request, "There was an error posting your comment. Please try again.")
        return super().form_invalid(form)

    def get_success_url(self):
        # Redirect to the same blog detail page
        return reverse_lazy('blog:blog_detail', kwargs={'pk': self.kwargs['pk']})
