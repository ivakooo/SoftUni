age = int(input())
wash_machine_price = float(input())
toy_price = int(input())

toys = 0
money = 0
saved_money = 0

for i in range(1, age+1):
    if i % 2 == 0:
        money += 10
        saved_money += money - 1

    else:
        toys += 1

total_money = saved_money + (toys * toy_price)

diff = abs(total_money - wash_machine_price)

if total_money >= wash_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
