from django.db import models
from mvc.models import User


class Size(models.Model):
    sku = models.CharField(max_length=20)
    slug = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_size')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_size')
    modified_date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return self.name

    class Meta:
        unique_together = (('sku',), ('slug',), ('name',))
