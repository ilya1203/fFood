from django.contrib import admin

# Register your models here.
from .models import Restoraunts

class RestAdmin(admin.ModelAdmin):
    list_display = ('name', 'long', 'width')
    list_display_links = ('name', 'long', 'width')
    search_fields = ('name', 'long', 'width')

admin.site.register(Restoraunts, RestAdmin)