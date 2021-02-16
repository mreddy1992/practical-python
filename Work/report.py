# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                portfolio.append((row[0], int(row[1]), float(row[2])))
            except ValueError:
                print("Bad input")

    return portfolio
