from django import forms
from bankinfo.models import *


class OperatingHourForm(forms.ModelForm):
    class Meta:
        model = OperatingHour
        fields = ['day', 'start', 'end']


class BaseForm(forms.Form):
    area = forms.CharField(max_length=50, label="Area ")
    address = forms.CharField(widget=forms.Textarea)
    district = forms.CharField(max_length=50, label="District ")
    latitude = forms.FloatField(label="Latitude ", initial=0.00)
    longitude = forms.FloatField(label="longitude ", initial=0.00)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.location:
            for f, d in self.instance.location.items():
                self.fields[f].initial = d
        # if self.instance.services:
        #     for f, d in self.instance.services.items():
        #         self.fields[f].initial = d

    def save(self, commit=True):
        instance = super().save(commit=False)

        fieldnames = ["area", "address", "district", "latitude", "longitude"]
        instance.location = {fieldname: self.cleaned_data[fieldname] for fieldname in fieldnames}

        if type(instance) == 'bankinfo.models.Branch':
            service_names = ["evening_banking", "remitance_transaction", "school_fees"]
            instance.services = {fieldname: self.cleaned_data[fieldname] for fieldname in service_names}

        if commit:
            instance.save()
        return instance


class BranchForm(BaseForm, forms.ModelForm):
    # services
    evening_banking = forms.BooleanField(label="Evening Banking ", required=False)
    remitance_transaction = forms.BooleanField(label="Remitance Transaction  ", required=False)
    school_fees = forms.BooleanField(label="School Fees ", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.services:
            for f, d in self.instance.services.items():
                self.fields[f].initial = d

    class Meta:
        model = Branch
        exclude = ["location", "services"]



class AtmBoothForm(BaseForm, forms.ModelForm):
    class Meta:
        model = AtmBooth
        exclude = ["location", "evening_banking", "remitance_transaction", "school_fees"]

