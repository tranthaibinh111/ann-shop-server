from django.db import models
from mvc.models import User
from .order import Order
from .product import Product


class OrderDetail(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    cost_of_goods = models.DecimalField(default=0, max_digits=9, decimal_places=0, help_text="Giá bán")
    price = models.DecimalField(default=0, max_digits=9, decimal_places=0, help_text="Giá bán")
    sale_price = models.DecimalField(default=0, max_digits=9, decimal_places=0, help_text="Giá bán trong thời kỳ giảm giá")
    discount = models.DecimalField(default=0, max_digits=9, decimal_places=0)
    total_price = models.DecimalField(default=0, max_digits=15, decimal_places=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_order_detail')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_order_detail')
    modified_date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return "{} bought {} clothes".format(str(self.customer), self.quantity, str(self.product))
