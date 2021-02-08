# pcost.py
import sys
import csv

def portfolio_cost(filename):

    total_price = 0.0
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)

    for row in rows:
        try:
            nshares = int(row[1])
            price_per_share = float(row[2].strip())
            total_price += (nshares * price_per_share)
        except ValueError:
            print("Bad row:", row)

    return total_price


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print(f'Total price of all stocks: {cost}')
