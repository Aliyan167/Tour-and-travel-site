from django.urls import path
from .views import BlogView,BlogDetailView

app_name = "blog"

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('blog-detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail')
]


