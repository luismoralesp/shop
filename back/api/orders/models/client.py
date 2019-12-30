from django.db import models
from api.commons.models import BaseModel
from ..constants import DocumentType

class Client(BaseModel):
    document = models.CharField(
        max_length=15
    )

    documentType = models.CharField(
        max_length=2,
        choices=DocumentType.choices
    )

    name = models.CharField(
        max_length=60
    )

    email = models.EmailField()

    surname = models.CharField(
        max_length=60
    )

    mobile = models.CharField(
        max_length=10
    )
