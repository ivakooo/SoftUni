product = input()
city = input()
quantity = float(input())

product_price = 0

if city == "Sofia":
    if product == "coffe":
        product_price = 0.50
    elif product == "water":
        product_price = 0.80
    elif product == "beer":
        product_price = 1.20
    elif product == "sweets":
        product_price = 1.45
    elif product == "peanuts":
        product_price = 1.60

elif city == "Plovdiv":
    if product == "coffe":
        product_price = 0.40
    elif product == "water":
        product_price = 0.70
    elif product == "beer":
        product_price = 1.15
    elif product == "sweets":
        product_price = 1.30
    elif product == "peanuts":
        product_price = 1.50

elif city == "Varna":
    if product == "coffe":
        product_price = 0.45
    elif product == "water":
        product_price = 0.70
    elif product == "beer":
        product_price = 1.10
    elif product == "sweets":
        product_price = 1.35
    elif product == "peanuts":
        product_price = 1.55
else:
    print("Wrong input!")

total_price = product_price * quantity

print(total_price)
