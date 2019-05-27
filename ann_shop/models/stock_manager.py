import uuid
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from enum import Enum
from mvc.models import User
from .product import Product


class StockFormality(Enum):
    I = "Input"
    O = "Output"


class StockManager(models.Model):
    __FORMALITY_CHOICES = [(tag.name, tag.value) for tag in StockFormality]

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_stock")
    formality = models.CharField(max_length=2, choices=__FORMALITY_CHOICES)
    quantity = models.IntegerField(default=0)
    quantity_current = models.IntegerField(default=0)
    note = RichTextUploadingField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_stock_manager')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_stock_manager')
    modified_date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return "Now, {} have {} ".format(str(self.product), self.quantity_current)
