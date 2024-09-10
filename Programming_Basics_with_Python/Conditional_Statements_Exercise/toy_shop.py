PUZZLE_PRICE = 2.60
DOLL_PRICE = 3
BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

price_of_trip = float(input())

number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

price_of_puzzles = number_of_puzzles * PUZZLE_PRICE
price_of_dolls = number_of_dolls * DOLL_PRICE
price_of_bears = number_of_bears * BEAR_PRICE
price_of_minions = number_of_minions * MINION_PRICE
price_of_trucks = number_of_trucks * TRUCK_PRICE

total_price = (price_of_puzzles + price_of_dolls + price_of_bears + price_of_minions
               + price_of_trucks)
total_toys = (number_of_puzzles + number_of_dolls + number_of_bears + number_of_minions
              + number_of_trucks)

if total_toys >= 50:
    total_price *= 0.75

total_price = total_price * 0.9

if total_price >= price_of_trip:
    print(f"Yes! {total_price - price_of_trip:.2f} lv left.")
else:
    print(f"Not enough money! {price_of_trip - total_price:.2f} lv needed.")