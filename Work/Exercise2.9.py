# report.py
#
# Exercise 2.9
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
                pass

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


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')
seprator = "-" * 10
print(
    f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(
    f'{seprator:>10s} {seprator:>10s} {seprator:>10s} {seprator:>10s}')

dollar_symbol = "$"
for name, shares, price, change in report:
    print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")
