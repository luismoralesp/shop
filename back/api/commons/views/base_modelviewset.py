from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet


class BaseModelViewSet(ModelViewSet):
    """Base modelviewset class"""

    serializer_classes = {
    }

    default_serializer_class = None

    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
