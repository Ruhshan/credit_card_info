from django.contrib import admin
from django import forms
from splitjson.widgets import SplitJSONWidget
from bankinfo.models import *
# Register your models here.
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday']


class BankDetailsInline(admin.StackedInline):
    model = BankDetails


# class BankForm(forms.ModelForm):
#     global days
#
#     def __init__(self, *args, **kwargs):
#         super(BankForm, self).__init__(*args, **kwargs)
#         # if self.instance.operating_hours:
#         #     o_times = self.instance.operating_hours
#         #     for d, t in o_times.items():
#         #         self.fields[d].initial = t
#
#     def save(self, commit=True):
#         global days
#         instance = super(BankForm, self).save(commit=False)
#
#
#         #instance.operating_hours = {day : self.cleaned_data[day] for day in days}
#         #instance.operating_hours=[{'day':day, 'start':self.cleaned_data[day].split('to')[0], 'end':self.cleaned_data[day].split('to')[1]} for day in days]
#
#
#         if commit:
#             instance.save()
#         return instance
#
#     class Meta:
#         model = Bank
#         #exclude = ['operating_hours']
#         fields =  '__all__'


class BankAdmin(admin.ModelAdmin):
    inlines = [BankDetailsInline,]
    # fieldsets = (
    #             ('Basic Info', {'fields': ('name',
    #                                         'circuit_id',
    #                                         'status'
    #                                         )
    #                             }
    #              ),
    #              ('Details', {'fields': ('about',
    #                                      'email',
    #                                      'phone',
    #                                      'camels',
    #                                      'earning_per_share',
    #                                      'address',
    #                                      )
    #                           }
    #               ),
    #              ('Operating Hours',
    #              {'fields': ('sunday',
    #                          'monday',
    #                          'tuesday',
    #                          'wednesday',
    #                          'thursday')
    #               }
    #               ),
    #              )

admin.site.register(Bank, BankAdmin)
admin.site.register(Branch)
admin.site.register(AtmBooth)
