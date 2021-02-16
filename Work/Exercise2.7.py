# report.py
#
# Exercise 2.7
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


def read_prices(filename):
    prices_dict = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            # print(row)
            try:
                prices_dict[row[0]] = float(row[1])
            except IndexError:
                print("Bad input")

    return prices_dict


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

# Calculate total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    total_cost += s['shares'] * s['price']

print('Total cost', total_cost)

# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += s['shares'] * prices[s['name']]

print('Current value', total_value)
print('Gain', total_value - total_cost)
