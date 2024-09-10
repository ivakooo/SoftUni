screening_type = input()
rows = int(input())
columns = int(input())

income = 0

cinema_capacity = rows * columns

PRICE_FOR_PREMIERE = 12
PRICE_FOR_NORMAL = 7.50
PRICE_DISCOUNT = 5

if screening_type == "Premiere":
    income = rows * columns * PRICE_FOR_PREMIERE
elif screening_type == "Normal":
    income = rows * columns * PRICE_FOR_NORMAL
elif screening_type == "Discount":
    income = rows * columns * PRICE_DISCOUNT

print(f"{income:.2f} leva")