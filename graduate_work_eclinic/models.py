import uuid

from django.db import models


class UUIDModel(models.Model):
    """Абстрактная модель, добавляющая поле id с uuid идентификатором."""

    id = models.UUIDField(
        verbose_name="идентификатор записи",
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__}:{self.id.hex}"
