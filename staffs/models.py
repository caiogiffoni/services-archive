import uuid

from django.db import models

from users.models import User

# Create your models here.


class Staff(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.TextField()
    startDate = models.DateField()
    quantity = models.PositiveIntegerField()
    area = models.TextField()
    role = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
