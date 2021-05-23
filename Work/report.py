#!/usr/bin/env python3
# report.py
#

# Import statements (libraries)
import sys
import csv
import fileparse

# Functions
def read_portfolio(filename):
    portfolio = fileparse.parse_csv(filename, 
                                    select=['name','shares','price'], 
                                    types=[str,int,float])

    return portfolio


def read_prices(filename):
    pricelist = fileparse.parse_csv(filename,
                                    types=[str,float], 
                                    has_headers=False)

    prices_dict = dict(pricelist)

    return prices_dict


def make_report(portfolio, prices):
    report = []
    for i in range(len(portfolio)):
        stock_name = (portfolio[i]['name'])
        # print(stock_name)
        stock_no_of_shares = (portfolio[i]['shares'])
        # print(stock_no_of_shares)
        stock_current_price = (prices[stock_name])
        # print(stock_current_price)
        stock_price_change = (stock_current_price - portfolio[i]['price'])
        # print(stock_price_change)
        report.append((stock_name, stock_no_of_shares,
                       stock_current_price, stock_price_change))

    return report


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    seprator = "-" * 10
    print(
        f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(
        f'{seprator:>10s} {seprator:>10s} {seprator:>10s} {seprator:>10s}')
    for name, shares, price, change in report:
        print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


# Main function
def main(argv):
    # Parse command line args, environment, etc.
    print(argv)
    if len(argv) != 3:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile pricefile')
    portfile = argv[1]
    pricefile = argv[2]
    report = portfolio_report(portfile, pricefile)


if __name__ == '__main__':
    import sys
    main(sys.argv)


# portfolio = read_portfolio('Data/portfolio.csv')
# prices = read_prices('Data/prices.csv')
# report = make_report(portfolio, prices)
# print_report(report)

# dollar_symbol = "$"
# for name, shares, price, change in report:
#     print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")







