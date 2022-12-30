import uuid

from django.db import models

from users.models import User

# Create your models here.


class Service(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    staff = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="service",
    )
    client = models.ForeignKey(
        "staffs.Staff",
        on_delete=models.CASCADE,
        related_name="service",
    )
