import uuid
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from mvc.models import User


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    note = RichTextUploadingField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_supplier')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_supplier')
    modified_date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return self.name

    class Meta:
        unique_together = ('name',)
