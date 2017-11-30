from django.contrib import admin
from django import forms
from splitjson.widgets import SplitJSONWidget
from bankinfo.models import *
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline
# Register your models here.
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday']

class OperatingHourForm(forms.ModelForm):
    class Meta:
        model = OperatingHour
        fields = ['day', 'start', 'end']


class OperatingHourInline(NestedTabularInline):
    model = OperatingHour
    max_num = 5
    form = OperatingHourForm

class BankDetailsInline(NestedStackedInline):
    model = BankDetails
    inlines = [OperatingHourInline]



class BankAdmin(NestedModelAdmin):
    inlines = [BankDetailsInline,]


admin.site.register(Bank, BankAdmin)
admin.site.register(Branch)
admin.site.register(AtmBooth)
