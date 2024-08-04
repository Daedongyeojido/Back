from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HashtagView.as_view())
]