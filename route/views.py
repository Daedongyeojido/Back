from django.shortcuts import render
from .models import Place
# Create your views here.
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Hello, this is the route app.")

def top_recommended_places(request):
    top_places = Place.objects.order_by('-place_like')[:3]
    places_data = [
        {
            "place_name": place.place_name,
            "place_address": place.place_address,
            "place_like": place.place_like
        }
        for place in top_places
    ]
    return JsonResponse({"top_recommended_places": places_data})