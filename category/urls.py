from django.urls import path, include
from .views import *

urlpatterns = [
    path('', CategorySave.as_view()),
    path('subCategory/<int:cId>', SubCategorySave.as_view()),
    path('categoryList/', CategoryList.as_view()),
    path('categoryInfo/<int:pk>', CategoryInfo.as_view())
]