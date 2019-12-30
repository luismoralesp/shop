from django.db import models
from api.commons.models import BaseModel
from . import Client
from ..constants import OrderStatus

class Order(BaseModel):
    """
    This is the model for the Orders
    """

    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices
    )

    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT
    )