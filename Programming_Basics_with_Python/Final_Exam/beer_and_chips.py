import math

BEER_PRICE = 1.20

fan_name = input()
budget = float(input())
bottles = int(input())
chips_packets = int(input())

total_beers_price = bottles * BEER_PRICE
chips_price = total_beers_price * 0.45
total_chips_price = math.ceil(chips_price * chips_packets)
final_price = total_beers_price + total_chips_price
difference = abs(budget - final_price)

if budget >= final_price:
    print(f"{fan_name} bought a snack and has {difference:.2f} leva left.")
else:
    print(f"{fan_name} needs {difference:.2f} more leva!")



