prices = []

while True:
    price = int(input("Enter price [0 to stop] :"))
    if price == 0:
        break

    prices.append(price)

prices.sort(reverse=True)

for price in prices:
    print(price, end=' ')
