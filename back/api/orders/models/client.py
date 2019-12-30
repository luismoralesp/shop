from django.db import models
from api.commons.models import BaseModel

class Client(BaseModel):
    document = models.CharField(
        max_length=15
    )

    documentType = models.CharField(
        max_length=2
    )

    name = models.CharField(
        max_length=60
    )

    surname = models.CharField(
        max_length=60
    )

    mobile = models.CharField(
        max_length=10
    )
