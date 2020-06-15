from django.contrib import admin

from core.models import Author, Post

admin.site.register(Post)
admin.site.register(Author)
