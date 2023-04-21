from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-'
    list_display = ('name', 'subject', 'created_date', 'email')
    search_fields = ('name', 'subject', 'message', 'email')

# admin.site.register(Post,PostAdmin)  # alterative way of registering
admin.site.register(Newsletter)