from django.contrib import admin
from blog.models import Post,Category
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', Category,'status','timestamp')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
