from django.contrib import admin
from .models import Ad, AdImage

class AdImageInline(admin.TabularInline):
    model = AdImage
    extra = 1

class AdAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'phone')
    inlines = [AdImageInline]

admin.site.register(Ad, AdAdmin)
