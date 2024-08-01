from django.db import models

class Hashtag:
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, default='', null=False)