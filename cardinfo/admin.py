from django.contrib import admin
from cardinfo.models import CreditCard, FileUpload
# Register your models here.

class CreditCardAdmin(admin.ModelAdmin):
    list_display = ('national_id', 'name_on_card', 'card_number', 'expire_on', 'card_cif','card_cvv','bank_cif')
    search_fields = ('national_id', 'name_on_card')

class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'csv_file', 'uploaded_at')
    #search_fields = ('national_id', 'name_on_card')

admin.site.register(CreditCard, CreditCardAdmin)
admin.site.register(FileUpload, FileUploadAdmin)
