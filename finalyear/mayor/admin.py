from django.contrib import admin
from .models import FileAdmin

class uploadadmin(admin.ModelAdmin):
    model=FileAdmin
    list_display = ['tittle','NIDNumber','HondingNo','wardno','is_published',]
    list_filter = ['tittle',]
    list_editable = ['is_published',]
    search_fields = ['NIDNumber',]

admin.site.register(FileAdmin,uploadadmin)

