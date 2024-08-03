from django.urls import path, include
from .views import *

urlpatterns = [
    path('', categorySave.as_view()),
    path('subCategory/<int:cId>', subCategorySave.as_view()),
]