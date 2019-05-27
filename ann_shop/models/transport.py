from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mvc.models import User


class Transport(MPTTModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    destination = models.CharField(max_length=255)
    prepay = models.BooleanField(default=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='transport_children')
    note = RichTextUploadingField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_transport')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_transport')
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
