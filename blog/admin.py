from django.contrib import admin
from .models import *

# Register your models here.

# @admin.register(Post)       # alterative way of registering
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-'
    list_display = ('title', 'author', 'created_date', 'publish_status','login_require', 'published_date')
    list_filter = ('publish_status','login_require', 'author',)
    #ordering = ('-created_date',)
    search_fields = ['title', 'content']

admin.site.register(Post,PostAdmin)
admin.site.register(Category)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-'
    list_display = ('name', 'subject', 'post',  'approved', 'created_date',)
    list_filter = ('approved',)
    ordering = ('-created_date',)
    search_fields = ('post', 'email', 'subject','name',)