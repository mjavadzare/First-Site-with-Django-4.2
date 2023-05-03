from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Project)       
class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-'
    list_display = ('title', 'author', 'created_date', 'publish_status', 'published_date')
    list_filter = ('publish_status', 'author',)
    #ordering = ('-created_date',)
    search_fields = ['title', 'content']

# admin.site.register(Post,PostAdmin) # alterative way of registering