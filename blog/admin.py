from django.contrib import admin
from .models import Post

# Registering admin access to blog post details
admin.site.register(Post)


