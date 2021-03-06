# report.py
#
# Exercise 2.5
import csv


def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio_dict = {}
            try:
                portfolio_dict['name'] = row[0]
                portfolio_dict['shares'] = int(row[1])
                portfolio_dict['price'] = float(row[2])
                portfolio.append(portfolio_dict)
            except ValueError:
                print("Bad input")

    return portfolio
