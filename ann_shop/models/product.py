from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from enum import Enum
from mvc.models import User
from .category import Category
from .supplier import Supplier
from .color import Color
from .size import Size


class ProductType(Enum):
    P = "Product"
    VP = "Variable Product"


class Product(MPTTModel):
    __KIND_CHOICES = [(tag.name, tag.value) for tag in ProductType]

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='product_children')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    kind = models.CharField(max_length=2, choices=__KIND_CHOICES)
    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    featured_image = models.ImageField(null=True, blank=True, help_text="Hình ảnh có SKU")
    clear_featured_image = models.ImageField(null=True, blank=True, help_text="Hình ảnh để quảng cáo")
    images = ArrayField(models.CharField(max_length=255))
    material = models.CharField(max_length=255, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True)
    minimum_inventory_level = models.IntegerField(default=0)
    max_inventory_level = models.IntegerField(default=0)
    quantity_stock = models.IntegerField(default=0)
    description = RichTextUploadingField(null=True, blank=True)
    variable = JSONField()
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_product')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_product')
    modified_date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return self.name

    class Meta:
        unique_together = ('name',)
