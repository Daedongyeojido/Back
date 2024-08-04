from django.db import models
from django.conf import settings


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(unique=True, default='', null=False, max_length=20)


class SubCategory(models.Model):
    subCategory_id = models.AutoField(primary_key=True)
    subCategory_name = models.CharField(unique=True, default='', null=False, max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False, related_name="subCategory")