import csv
import re

from django.contrib.gis.geos import GEOSGeometry
from map.models import Node

Node.objects.all().delete()
files = [
    './data/node_문캠.csv',
    './data/node_이캠.csv'
]
count = 0
for file in files:
    with open(file, 'r', encoding='utf-8') as rf:
        reader = csv.reader(rf)
        next(reader)
        for line in reader:
            count += 1
            print(count, line[0], line[3], line[2])
            Node.objects.create(
                id=count,
                name=re.sub(r'\s|_', '', line[0]),
                point=GEOSGeometry(f'POINT({line[3]} {line[2]})')
            )
