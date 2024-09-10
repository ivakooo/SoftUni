budget = float(input())
staff = int(input())
wear_price = float(input())

decor_amount = budget * 0.1
total_wear_price = staff * wear_price

if staff > 150:
    total_wear_price = total_wear_price - (total_wear_price * 0.1)

total_amount = decor_amount + total_wear_price
difference = abs(budget - total_amount)

if total_amount > budget:
    print(f"Not enough money!\nWingard needs {difference:.2f} leva more.")
else:
    print(f"Action!\nWingard starts filming with {difference:.2f} leva left.")
