from rest_framework import serializers
from ..models import Order, Client
from ..constants import OrderStatus

class OrderCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = (
            '__all__'
        )

    def create(self, validated_data):
        client = super().create(validated_data)
        return Order.objects.create(
            status = OrderStatus.CREATED,
            client = client
        )
