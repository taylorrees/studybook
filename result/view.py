import csv
from templates.table import Table

def main(test_id, name):
    results = []

    with open('results/' + str(test_id) + '.csv', 'r') as csvfile:
        rdr = csv.reader(csvfile)
        for row in rdr:
            results.append(row)

    Table('Results For: ' + name , results)