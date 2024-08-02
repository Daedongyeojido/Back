import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "greenroute.settings")
django.setup()

from route.models import Place



CSV_PATH = "C:/Users/jiyou/Desktop/멋쟁이사자처럼/중앙해커톤/back/data.csv"

with open(CSV_PATH, newline='', encoding='cp949') as csvfile:
	data_reader = csv.reader(csvfile)
	for row in data_reader:
		print(row)
		Place.objects.create(
            place_name = row[1],
            place_address = row[2],
            place_latitude = row[3],
            place_longitude = row[4],
            place_like = row[6],
            subCategory_id = row[5]
        )
