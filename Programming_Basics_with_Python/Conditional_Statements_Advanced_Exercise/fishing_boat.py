budget = int(input())
season = input()
crew = int(input())

rent_price = 0

# Сезон - текст: "Spring", "Summer", "Autumn" или "Winter";

if season == "Spring":
    rent_price = 3000
elif season == "Winter":
    rent_price = 2600
else:
    rent_price = 4200  # for  Summer and Autumn

if crew <= 6:
    rent_price = rent_price * 0.9
elif 7 <= crew <= 11:
    rent_price = rent_price * 0.85
else:
    rent_price = rent_price * 0.75

if season != "Autumn" and crew % 2 == 0:
    rent_price = rent_price * 0.95


if budget >= rent_price:
    print(f"Yes! You have {budget - rent_price:.2f} leva left.")
elif budget < rent_price:
    print(f"Not enough money! You need {rent_price - budget:.2f} leva.")


