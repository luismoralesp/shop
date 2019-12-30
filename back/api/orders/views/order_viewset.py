from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from api.commons.views import BaseModelViewSet
from ..serializers import OrderCreationSerializer, OrderOutputSerializer
from drf_yasg.utils import swagger_auto_schema
from ..models import Order


class OrderViewSet(BaseModelViewSet):
    """API to manage orders"""

    serializer_classes = {
        'list': OrderOutputSerializer,
        'retrieve': OrderOutputSerializer,
        'create': OrderCreationSerializer
    }

    default_serializer_class = OrderOutputSerializer

    queryset = Order.objects.all()

    http_method_names = ['post']

    @swagger_auto_schema(responses={200: OrderOutputSerializer()} )
    def create(self, request, *args, **kwargs):
        """ Endpoint to create a new order """
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        order = serializer.save()
        data = OrderOutputSerializer(order).data
        
        return Response(data, status=status.HTTP_201_CREATED)



