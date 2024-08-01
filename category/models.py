from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, default='', null=False)


class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, default='', null=False)
    category = models.ForeignKey(Category, realted_name="category", on_delete=models.CASCADE, null=False, blank=False)