from django.db import models
from django.conf import settings
from route.models import Route

class Hashtag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, default='', null=False, max_length=20)
    route = models.ManyToManyField(Route, related_name="route")