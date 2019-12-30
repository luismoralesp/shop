from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid


class BaseModel(models.Model):
    """
    Base for all models
    """
    uuid = models.UUIDField(
        verbose_name=_('Unique Identifier'),
        help_text=_('Unique Identifier.'),
        unique=True,
        default=uuid.uuid4,
        editable=False)

    created_at = models.DateTimeField(
        verbose_name=_('Date Created'),
        help_text=_('Creation Date.'),
        auto_now_add=True)

    updated_at = models.DateTimeField(
        verbose_name=_('Date Updated'),
        help_text=_('Last Update.'),
        auto_now=True)

    class Meta:
        abstract = True
