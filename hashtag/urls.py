from django.urls import path, include
from .views import *

urlpatterns = [
    path('hashtagList', HashtagView.as_view()),
    path('routes/<int:route_id>/hashtag/<int:hashtag_id>', RouteHashtag.as_view())
]