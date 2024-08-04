from django.db import models
from django.conf import settings

class Hashtag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, default='', null=False, max_length=20)
