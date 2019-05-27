from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mvc.models import User


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='category_children')
    description = RichTextUploadingField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_category')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_category')
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        unique_together = ('parent', 'name')
        order_insertion_by = ['name']
        verbose_name_plural = "Categories"
