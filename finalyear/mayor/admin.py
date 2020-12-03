from django.contrib import admin
from .models import FileAdmin,OfficerMeeting

class uploadadmin(admin.ModelAdmin):
    model=FileAdmin
    list_display = ['tittle','NIDNumber','HondingNo','wardno','is_published',]
    list_filter = ['tittle',]
    list_editable = ['is_published',]
    search_fields = ['NIDNumber',]

admin.site.register(FileAdmin,uploadadmin)


class OfficermeetingAdmin(admin.ModelAdmin):
    model=OfficerMeeting
    list_display = ['title','date','time','day']
    list_editable = ['date','time','day']
    search_fields = ['title']


admin.site.register(OfficerMeeting,OfficermeetingAdmin)

