from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class HealthView(APIView):
    """Endpoint to know the status of the API """

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        data = {"health": "good"}
        return Response(data)

    @classmethod
    def get_extra_actions(cls):
        return []