from django.contrib import admin
from .models import Category, Tag, BlogPost


# Admin for Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Displays the name of the category
    search_fields = ('name',)  # Adds a search bar for categories


# Admin for Tag model
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Displays the name of the tag
    search_fields = ('name',)  # Adds a search bar for tags


# Admin for BlogPost model
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')  # Display title, author, and date in the list view
    list_filter = ('categories', 'tags', 'publication_date')  # Filters for categories, tags, and date
    search_fields = ('title', 'author', 'content')  # Search bar for title, author, and content
    filter_horizontal = ('categories', 'tags')  # Makes ManyToMany fields easier to manage
