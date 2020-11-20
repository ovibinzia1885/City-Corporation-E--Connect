from django.contrib import admin
from public.models import ApplyLicence,HomeApplication,HomeTax,Onlinebdapply

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

class HomeTaxAdmin(admin.ModelAdmin):

    class Meta:
        model=HomeTax

    list_display = ['name','ward_no','HoldingNo','pictureowner']
    list_filter = ['HoldingNo',]
    list_display_links = ['HoldingNo',]
    search_fields = ['HoldingNo',]
admin.site.register(HomeTax,HomeTaxAdmin)

class onlinebdAdmin(admin.ModelAdmin):

    class Meta:
        model=Onlinebdapply

    list_display = ['name','PersonalNumber','FatherName','MotherName','BithofDate','PresentAddress','Gender','subdistict']
    list_filter = ['PersonalNumber',]
    list_display_links = ['PersonalNumber',]
    search_fields = ['PersonalNumber',]
admin.site.register(Onlinebdapply,onlinebdAdmin)


