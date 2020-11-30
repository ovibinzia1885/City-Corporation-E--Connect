from django.contrib import admin
from .models import Workshop,uploadbudget


class workshopAdmin(admin.ModelAdmin):
    model=Workshop
    list_display = ['tittle','type','duriation','photo_main','is_published']
    list_filter = ['tittle',]
    list_display_links = ['tittle',]
    search_fields = ['tittle',]
admin.site.register(Workshop,workshopAdmin)

admin.site.register(uploadbudget)