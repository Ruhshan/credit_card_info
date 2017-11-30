from rest_framework import serializers, viewsets
from bankinfo.serializers import *

class BankRetrive(viewsets.ModelViewSet):
    serializer_class = BankSerializer
    queryset = Bank.objects.select_related().all()
