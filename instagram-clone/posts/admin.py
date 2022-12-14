from django.contrib import admin
from .models import Post, PostComment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["user", "created", "image", "edit_time", "slug", "edited"]
    list_filter = ("created", "edited")
    
@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "id"]
    