from django.contrib import admin
from public.models import ApplyLicence,HomeApplication

class ApplyLicenceAdmin(admin.ModelAdmin):

    class Meta:
        model=ApplyLicence

    list_display = ['name','FatherName','NIDNumber','ward','type']
    list_filter = ['NIDNumber']
    list_display_links = ['ward']
    search_fields = ['name','NIDNumber','ward','type']
admin.site.register(ApplyLicence,ApplyLicenceAdmin)

class HomeApplicationAdmin(admin.ModelAdmin):

    class Meta:
        model = HomeApplication

    list_display = ['name','FatherName','NIDNumber','wardno','SelectFloor','PreviousTax','pic']
    list_filter = ['NIDNumber']
    list_display_links = ['name']
    search_fields = ['name','NIDNumber','wardno']
admin.site.register(HomeApplication,HomeApplicationAdmin)
