from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('top_recommended_places/', views.top_recommended_places, name='top_recommended_places'),
]