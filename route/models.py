from django.db import models
from users.models import MyUser
from category.models import SubCategory

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
    places = models.ManyToManyField('Place', through='Route_places', related_name='routes')


class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=50)
    place_address = models.CharField(max_length=100)
    place_like = models.IntegerField()
    place_latitude = models.FloatField()
    place_longitude = models.FloatField()
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)


class Route_places(models.Model):
    route_places_id = models.AutoField(primary_key=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    user_like = models.BooleanField()
