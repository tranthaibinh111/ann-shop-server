from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from mvc.models import User


class Shipper(models.Model):
    name = models.CharField(max_length=100)
    name_unicode = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    note = RichTextUploadingField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_shipper')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_shipper')
    modified_date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'phone')
