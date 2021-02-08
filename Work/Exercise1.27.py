
f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
# print(headers)
total_price = 0

for line in f:
    row = line.split(',')
    price = int(row[1]) * float(row[2].strip())
    total_price += price
    # print(row)
f.close()
print(f'Total price of all stocks: {total_price}')
