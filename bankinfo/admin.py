from django.contrib import admin
from django import forms
from bankinfo.models import *
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline
from bankinfo.forms import *
# Register your models here.

class OperatingHourInline(NestedTabularInline):
    model = OperatingHour
    max_num = 5
    form = OperatingHourForm

class BankDetailsInline(NestedStackedInline):
    model = BankDetails
    inlines = [OperatingHourInline]


class BankAdmin(NestedModelAdmin):
    inlines = [BankDetailsInline,]


class BranchAdmin(admin.ModelAdmin):
    form = BranchForm

class AtmBoothAdmin(admin.ModelAdmin):
    form = AtmBoothForm

admin.site.register(Bank, BankAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(AtmBooth, AtmBoothAdmin)
