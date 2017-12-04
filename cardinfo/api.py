from django.db.models import Q

from rest_framework import serializers, viewsets, generics
from cardinfo.serializers import *


class CardRetrive(generics.ListAPIView):
    serializer_class = CardSerializer

    def get_queryset(self):
        bank_cif = self.request.GET.get('bank_cif') or None
        card_cif = self.request.GET.get('card_cif') or None
        return CreditCard.objects.filter(Q(bank_cif=bank_cif) | Q(card_cif=card_cif))
