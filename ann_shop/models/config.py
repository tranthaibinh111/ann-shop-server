from django.db import models
from mvc.models import *


class Config(models.Model):
    number_date_change = models.IntegerField(default=0, help_text="Số ngày cho phép đổi sản phẩm")
    number_of_change_product = models.IntegerField(default=0, help_text="Số lượng sản phẩm cho phép đổi")
    fee_of_change = models.DecimalField(default=0, max_digits=9, decimal_places=0, help_text="Phí đổi sản phẩm")
    note_of_order = models.CharField(max_length=255, help_text="Ghi chu thích cuối đơn hàng")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_config')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_config')
    modified_date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return "Config #{}".format(self.pk)
