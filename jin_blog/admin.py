from django.contrib import admin
from jin_blog.models import Post, Page

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    fields = ["published", "title", "slug", "content", "author"]
    list_display = ["published", "title", "updated"]
    list_display_links = ["title"]
    list_editable = ["published"]
    list_filter = ["published", "updated", "author"]
    search_fields = ["title", "content"]

class PageAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    fields = ["published", "title", "slug", "content", "author"]
    list_display = ["published", "title", "updated"]
    list_display_links = ["title"]
    list_editable = ["published"]
    list_filter = ["published", "updated", "author"]
    search_fields = ["title", "content"]

admin.site.register(Post, PostAdmin)
admin.site.register(Page, PageAdmin)
