
def portfolio_cost(filename):

    f = open(filename, 'rt')
    headers = next(f).split(',')
    # print(headers)
    total_price = 0

    for line in f:
        row = line.split(',')
        nshares = int(row[1])
        price_per_share = float(row[2].strip())
        price_for_given_stock = nshares * price_per_share
        total_price += price_for_given_stock
        # print(row)
    f.close()
    print(f'Total price of all stocks: {total_price}')
