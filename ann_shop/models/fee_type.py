from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from mvc.models import User


class FeeType(models.Model):
    name = models.CharField(max_length=255)
    is_negative = models.BooleanField(default=False)
    note = RichTextUploadingField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_product')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_product')
    modified_date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return self.name

    class Meta:
        unique_together = ('name',)
