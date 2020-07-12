from rest_framework import serializers
from APIapp.models import *

class CardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Card
        depth=2
        fields=('cc_number', 'expirationMonth', 'expirationYear', 'cvv',)

class TxnSerializer(serializers.ModelSerializer):
    card=CardSerializer(read_only=False)

    class Meta:
        model=Transaction
        depth=2
        fields=('amount', 'currency', 'card_type', 'card')

    def create(self, validated_data):
        card_data = validated_data.pop('card')
        card = Card.objects.create(**card_data)
        txn = Transaction.objects.create(card=card, **validated_data)
        return txn
