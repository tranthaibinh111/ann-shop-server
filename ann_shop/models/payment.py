import uuid
from datetime import datetime
from django.db import models
from enum import Enum
from mvc.models import User
from .order import Order
from .account_bank import AccountBank


class PaymentType(Enum):
    C = "Cash"
    T = "Transfer"
    CL = "Collection"
    D = "Debt"


class PaymentStatus(Enum):
    UP = "Unpaid"
    PNE = "Payment don't enough"
    C = "Paid"


class Payment(models.Model):
    __TYPE_CHOICES = [(tag.name, tag.value) for tag in PaymentType]
    __STATUS_CHOICES = [(tag.name, tag.value) for tag in PaymentStatus]

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_payment')
    type = models.CharField(max_length=2, choices=__TYPE_CHOICES, null=True, blank=True)
    status = models.CharField(max_length=2, choices=__STATUS_CHOICES, null=True, blank=True)
    account_bank = models.ForeignKey(AccountBank, on_delete=models.SET_NULL, null=True, blank=True)
    money = models.DecimalField(default=0, max_digits=20, decimal_places=0)
    done_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_payment')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_payment')
    modified_date = models.DateTimeField(auto_now=True)

    def __init__(self):
        message = "Order #{} done payment at".format(self.order.pk)
        if isinstance(self.done_at, datetime):
            message = message + self.done_at.strftime('%Y/%m/%d')
        return message
