__author__ = 'regrant'

import csv

tab_csv = open("/Users/regrant/GDL Code/Source Files/HI DD/ALL 384 well data HHT-2994 a.csv", 'rb')
reader = csv.reader(tab_csv, dialect='excel-tab')

output_csv = open("/Users/regrant/GDL Code/Source Files/HI DD/test output.csv", 'rb')
writer = csv.writer(output_csv, dialect='excel-tab')

for row in reader


tab_csv.close()
output_csv.close()