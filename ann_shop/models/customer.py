import uuid
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from mvc.models import User


class Customer(models.Model):
    avatar = models.ImageField(upload_to="{}/{}".format(settings.CUSTOMER_AVATAR_PATH, uuid), null=True, blank=True)
    nick = models.CharField(max_length=100)
    nick_unicode = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    name_unicode = models.CharField(max_length=100)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    zalo_phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, help_text="Địa chỉ khách hàng")
    note = RichTextUploadingField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_customer')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_customer')
    modified_date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'phone1')
