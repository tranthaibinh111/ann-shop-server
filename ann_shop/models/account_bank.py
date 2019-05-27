from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from mvc.models import User
from .bank import Bank


class AccountBank(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=50)
    account_name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    note = RichTextUploadingField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_account_bank')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_account_bank')
    modified_date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return "{}: {}".format(self.account_name, self.bank)

    class Meta:
        unique_together = ('bank', 'account_number')
