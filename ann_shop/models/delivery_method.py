from django.db import models
from enum import Enum
from mvc.models import User


class DeliveryType(Enum):
    TP = "Take place"
    PO = "Post office"
    SS = "Shipping service"
    HC = "House car"
    DD = "Direct delivery"


class DeliveryMethod(models.Model):
    __KIND_CHOICES = [(tag.name, tag.value) for tag in DeliveryType]

    kind = models.CharField(max_length=2, choices=__KIND_CHOICES, null=True, blank=True)
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_delivery_method')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_delivery_method')
    modified_date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return self.name

    class Meta:
        unique_together = ('name',)
