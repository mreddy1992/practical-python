#!/usr/bin/env python3
# pcost.py
#

import csv
import report

# def read_portfolio(filename):
#     portfolio = []

#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             portfolio_dict = {}
#             try:
#                 portfolio_dict['name'] = row[0]
#                 portfolio_dict['shares'] = int(row[1])
#                 portfolio_dict['price'] = float(row[2])
#                 portfolio.append(portfolio_dict)
#             except ValueError:
#                 print("Bad input")

#     return portfolio


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


def portfolio_cost(portfolio):
    total_cost = 0.0
    for s in portfolio:
        total_cost += s['shares'] * s['price']

    print('Total cost', total_cost)


# Main function
def main(argv):
    # Parse command line args, environment, etc.
    print(argv)
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile')
    portfile = argv[1]
    portfolio = report.read_portfolio(portfile)
    # Calculate total cost of the portfolio
    portfolio_total_cost = portfolio_cost(portfolio)


if __name__ == '__main__':
    import sys
    main(sys.argv)

# portfolio = report.read_portfolio('Data/portfolio.csv')
# prices = read_prices('Data/prices.csv')

# # Calculate total cost of the portfolio
# portfolio_cost = portfolio_cost(portfolio)

# Calculate total cost of the portfolio
# total_cost = 0.0
# for s in portfolio:
#     total_cost += s['shares'] * s['price']

# print('Total cost', total_cost)

# Compute the current value of the portfolio
# total_value = 0.0
# for s in portfolio:
#     total_value += s['shares'] * prices[s['name']]

# print('Current value', total_value)
# print('Gain', total_value - total_cost)
