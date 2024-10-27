prices = [100, 90, 7.99, 24.99, 30, 55, 999.99]
z  = range(1, 1000, 50)


x = 0
for item in prices: 
    x = x + item

print(x)
print(z)
for item in z:
    print(item)

print(prices)