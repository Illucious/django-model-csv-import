from django.contrib import admin
from .models import Phones
# Register your models here.

class PhonesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rating', 'image', 'url')

admin.site.register(Phones, PhonesAdmin)