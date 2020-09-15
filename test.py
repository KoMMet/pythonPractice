import sys
import csv
import pprint

with open('data/A_20200831_1.csv', 'r', encoding='shift_jisx0213') as f:
    csv_r = csv.reader(f, delimiter=',', quotechar='"')
    for row in csv_r:
        print(','.join(row))


