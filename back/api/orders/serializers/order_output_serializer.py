from rest_framework import serializers
from . import ClientOutputSerializer
from ..models import Order

class OrderOutputSerializer(serializers.ModelSerializer):
    
    client = ClientOutputSerializer()

    class Meta:
        model = Order
        fields = (
            'uuid',
            'status',
            'client'
        )
