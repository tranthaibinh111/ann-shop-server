from django.db import models
from enum import Enum
from mvc.models import User
from .order import Order
from .delivery_method import DeliveryMethod
from .shipper import Shipper
from .transport import Transport


class DeliveryStatus(Enum):
    D = "Delivered"
    S = "Shipping"
    PD = "Prepare for delivery"


class FormalityType(Enum):
    N = "Normal"
    F = "Faster"


class Delivery(models.Model):
    __STATUS_CHOICES = [(tag.name, tag.value) for tag in DeliveryStatus]
    __FORMALITY_CHOICES = [(tag.name, tag.value) for tag in FormalityType]

    order = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
    method = models.ForeignKey(DeliveryMethod, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=__STATUS_CHOICES, null=True, blank=True)
    formality = models.CharField(max_length=2, choices=__FORMALITY_CHOICES, null=True, blank=True)
    shipping_code = models.CharField(max_length=255, null=True, blank=True, help_text="Mã đơn của dịch vụ vận chuyển")
    shipper = models.ForeignKey(Shipper, on_delete=models.SET_NULL, null=True, blank=True, help_text="Người giao hàng")
    shipping_fee = models.DecimalField(default=0, max_digits=9, decimal_places=0, help_text="Phí của nhân viên giao hàng")
    transport = models.ForeignKey(Transport, on_delete=models.SET_NULL, null=True, blank=True)
    invoice_image = models.ImageField(null=True, blank=True)
    done_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_delivery')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_delivery')
    modified_date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return "Order #{} {}".format(self.order.pk, str(self.method))

    class Meta:
        unique_together = ('order',)
