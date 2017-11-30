from rest_framework import serializers, generics, viewsets

from bankinfo.models import Bank, AtmBooth, BankDetails

class

class BankDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetails
        exclude = ["id"]


class AtmBoothSerializer(serializers.ModelSerializer):

    class Meta:
        model = AtmBooth
        exclude = ["bank"]


class BankSerializer(serializers.ModelSerializer):
    atm_booths = AtmBoothSerializer(many=True)
    details = BankDetailSerializer()

    class Meta:
        model = Bank
        fields = '__all__'


class BankRetrive(viewsets.ModelViewSet):
    serializer_class = BankSerializer
    queryset = Bank.objects.select_related().all()
