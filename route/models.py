from django.db import models
from users.models import *

# Create your models here.
class Route(models.Model):
  route_id = models.AutoField(primary_key=True)
  startpoint_name = models.CharField(max_length=50)
  startpoint_address = models.CharField(max_length=50)
  startpoint_x = models.IntegerField()
  startpoint_y = models.IntegerField()
  endpoint_name = models.CharField(max_length=50)
  endpoint_address = models.CharField(max_length=50)
  endpoint_x = models.IntegerField()
  endpoint_y = models.IntegerField()
  date = models.DateField()
  user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)

class Place(models.Model):
  place_id = models.AutoField(primary_key=True)
  place_name = models.CharField(max_length=50)
  place_address = models.CharField(max_length=50)
  place_like = models.IntegerField()
  place_x = models.IntegerField()
  place_y = models.IntegerField()
  # category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
  subcategory_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

class Route_places(models.Model):
  route_places_id = models.AutoField(primary_key=True)
  route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
  user_like = models.BooleanField()