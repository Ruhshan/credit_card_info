from rest_framework import serializers
from bankinfo.models import Bank, AtmBooth, BankDetails, Branch, OperatingHour



class OperatingHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingHour
        exclude = ["id", "details"]

class BankDetailSerializer(serializers.ModelSerializer):
    operating_hours = OperatingHourSerializer(many = True)
    class Meta:
        model = BankDetails
        exclude = ["bank", "id"]


class AtmBoothSerializer(serializers.ModelSerializer):

    class Meta:
        model = AtmBooth
        exclude = ["bank"]

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        exclude = ["bank"]

class BankSerializer(serializers.ModelSerializer):
    atm_booths = AtmBoothSerializer(many=True)
    branches = BranchSerializer(many=True)
    details = BankDetailSerializer()

    class Meta:
        model = Bank
        fields = '__all__'
