from django.db import models
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='blog_posts')
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    description = HTMLField(default='No content available')
    image1 = models.ImageField(upload_to="tour_images/", null=True, blank=True)
    image2 = models.ImageField(upload_to="tour_images/", null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey('BlogPost', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=200)
    comment = models.TextField()

    def __str__(self):
        return self.title
