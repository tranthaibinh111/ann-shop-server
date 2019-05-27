from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mvc.models import User


class Bank(MPTTModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='bank_children')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_bank')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_bank')
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.is_root_node():
            return self.name
        else:
            if self.parent:
                return "{} - {}".format(self.parent.name, self.name)
            else:
                return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
        unique_together = ('parent', 'name')
