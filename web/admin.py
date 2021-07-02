from django.contrib import admin
from .models import Author, Post

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','username')
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'body')
    prepopulated_fields = {'slug': ('title',)}
