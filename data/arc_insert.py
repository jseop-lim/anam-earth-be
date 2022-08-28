import csv
import re

from map.models import Node, Arc

Arc.objects.all().delete()
files = [
    './data/arc_문캠.csv',
    './data/arc_이캠.csv'
]
count = 0
for file in files:
    with open(file, 'r', encoding='utf-8') as rf:
        reader = csv.reader(rf)
        next(reader)
        for line in reader:
            try:
                node1 = Node.objects.get(name=re.sub(r'\s|_', '', line[0]))
                node2 = Node.objects.get(name=re.sub(r'\s|_', '', line[1]))
                field_values = dict(
                    vertical_distance=float(line[2]),
                    horizontal_distance=float(line[3]),
                    is_stair=int(line[5]),
                    is_step=int(line[6]),
                    quality=line[7],
                )
                count += 1
                Arc.objects.create(id=count, start_node=node1, end_node=node2, **field_values)
            except Node.DoesNotExist as e:
                print(e, file, line[0], line[1])
                break
            except ValueError as e:
                print(e)
