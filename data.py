import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "greenroute.settings")
django.setup()

from route.models import Place
from category.models import *
from hashtag.models import Hashtag



CSV_PATH_1 = "C:/Users/jiyou/Desktop/멋쟁이사자처럼/중앙해커톤/back/csv/category.csv"
CSV_PATH_2 = "C:/Users/jiyou/Desktop/멋쟁이사자처럼/중앙해커톤/back/csv/subCategory.csv"
CSV_PATH_3 = "C:/Users/jiyou/Desktop/멋쟁이사자처럼/중앙해커톤/back/csv/data.csv"
CSV_PATH_4 = "C:/Users/jiyou/Desktop/멋쟁이사자처럼/중앙해커톤/back/csv/hashtag.csv"



with open(CSV_PATH_1, newline='', encoding='UTF-8-sig') as csvfile:
	data_reader = csv.reader(csvfile)
	for row in data_reader:
		print(row)
		Category.objects.create(
            category_name = row[0]
        )
		
with open(CSV_PATH_2, newline='', encoding='UTF-8-sig') as csvfile:
	data_reader = csv.reader(csvfile)
	for row in data_reader:
		print(row)
		SubCategory.objects.create(
            subCategory_name = row[0],
			category = Category.objects.get(category_id = row[1])
        )

with open(CSV_PATH_3, newline='') as csvfile:
	data_reader = csv.reader(csvfile)
	for row in data_reader:
		print(row)
		Place.objects.create(
            place_name = row[1],
            place_address = row[2],
            place_latitude = row[3],
            place_longitude = row[4],
            place_like = row[6],
            subCategory = SubCategory.objects.get(subCategory_id = row[5])
        )

with open(CSV_PATH_4, newline='', encoding='UTF-8-sig') as csvfile:
	data_reader = csv.reader(csvfile)
	for row in data_reader:
		print(row)
		Hashtag.objects.create(
            name = row[0]
        )
