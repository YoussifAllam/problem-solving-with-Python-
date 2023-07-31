x, p = map(int, input().split())
original_price = (100 * p) / (100 - x)
original_price = round(original_price, 2)

print(original_price)