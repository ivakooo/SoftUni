fruit = input()
day = input()
quantity = float(input())

fruit_price = 0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        fruit_price = 2.50
    elif fruit == "apple":
        fruit_price = 1.20
    elif fruit == "orange":
        fruit_price = 0.85
    elif fruit == "grapefruit":
        fruit_price = 1.45
    elif fruit == "kiwi":
        fruit_price = 2.70
    elif fruit == "pineapple":
        fruit_price = 5.50
    elif fruit == "grapes":
        fruit_price = 3.85
    else:
        print("error")
        exit()

elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        fruit_price = 2.70
    elif fruit == "apple":
        fruit_price = 1.25
    elif fruit == "orange":
        fruit_price = 0.90
    elif fruit == "grapefruit":
        fruit_price = 1.60
    elif fruit == "kiwi":
        fruit_price = 3.00
    elif fruit == "pineapple":
        fruit_price = 5.60
    elif fruit == "grapes":
        fruit_price = 4.20
    else:
        print("error")
        exit()

else:
    print("error")
    exit()

total_price = fruit_price * quantity
print (f"{total_price:.2f}")
