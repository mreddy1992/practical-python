# report.py
#
# Exercise 2.6
import csv


def read_prices(filename):
    prices_dict = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            print(row)
            try:
                prices_dict[row[0]] = float(row[1])
            except IndexError:
                print("Bad input")

    return prices_dict
