import uuid
from django.db import models
from enum import Enum
from mvc.models import User
from .customer import Customer


class OrderType(Enum):
    W = "Wholesale"
    R = "Retail"


class OrderStatus(Enum):
    P = "Processing"
    D = "Done"
    C = "Cancelled"


class Order(models.Model):
    __KIND_CHOICES = [(tag.name, tag.value) for tag in OrderType]
    __STATUS_CHOICES = [(tag.name, tag.value) for tag in OrderStatus]

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    kind = models.CharField(max_length=2, choices=__KIND_CHOICES, null=True, blank=True)
    status = models.CharField(max_length=2, choices=__STATUS_CHOICES, null=True, blank=True)
    total_discount = models.DecimalField(default=0, max_digits=15, decimal_places=0, help_text="Tổng số tiền triết khấu")
    tool_fee = models.DecimalField(default=0, max_digits=15, decimal_places=0, help_text="Tổng phí của đổi trả và phí khác")
    tool_price = models.DecimalField(default=0, max_digits=20, decimal_places=0, help_text="Tổng giá")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_order')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_order')
    modified_date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return "Order of {}: {}".format(str(self.customer), self.uuid)
