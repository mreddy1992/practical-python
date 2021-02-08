

def portfolio_cost(filename):

    total_price = 0.0

    with open(filename, 'rt') as f:
        headers = next(f).split(',')

        for line in f:
            row = line.split(',')
            try:
                nshares = int(row[1])
                price_per_share = float(row[2].strip())
                total_price += (nshares * price_per_share)
            except ValueError:
                print("Bad row:", row)
    print(f'Total price of all stocks: {total_price}')
