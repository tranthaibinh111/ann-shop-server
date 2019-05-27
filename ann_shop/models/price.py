from django.db import models
from mvc.models import User
from .product import Product


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_price')
    is_sale = models.BooleanField(default=False)
    cost_of_goods = models.DecimalField(default=0, max_digits=9, decimal_places=0, help_text="Tiền vốn")
    regular_price = models.DecimalField(default=0, max_digits=9, decimal_places=0, help_text="Giá sỉ")
    retail_price = models.DecimalField(default=0, max_digits=9, decimal_places=0, help_text="Giá lẻ")
    last_price = models.ForeignKey("Price", on_delete=models.SET_NULL, null=True, blank=True, help_text="Giá lần trước")
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_price')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_price')
    modified_date = models.DateTimeField(auto_now=True)

    def __init__(self):
        if self.is_sale:
            return "Giá sale {}".format(self.modified_date.strftime('%Y/%m/%d'))
        else:
            return "Giá {}".format(self.modified_date.strftime('%Y/%m/%d'))
