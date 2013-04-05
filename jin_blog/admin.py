from django.contrib import admin
from jin_blog.models import Post

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    fields = ["published", "title", "slug", "content", "author"]
    list_display = ["published", "title", "updated"]
    list_display_links = ["title"]
    list_editable = ["published"]
    list_filter = ["published", "updated", "author"]
    search_fields = ["title", "content"]
    # change_form_template = 'jin_blog/admin/change_form.html'

admin.site.register(Post, PostAdmin)
