n = int(input().strip())
price = [int(x) for x in input().strip().split(" ")]

loss = max(price)
priceSorted = sorted(price)
for i in range(n-1):
    if priceSorted[i+1] - priceSorted[i] < loss and price.index(priceSorted[i+1]) < price.index(priceSorted[i]):
            loss = priceSorted[i+1] - priceSorted[i]
print(loss)