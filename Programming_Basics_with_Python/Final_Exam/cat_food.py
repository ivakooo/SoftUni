FOOD_PRICE_PER_1KG = 12.45

numbers_cats = int(input())

group1 = 0
group2 = 0
group3 = 0
total_grams = 0

for i in range(numbers_cats):
    food_grams = float(input())
    if 100 <= food_grams < 200:
        group1 += 1
    elif 200 <= food_grams < 300:
        group2 += 1
    elif 300 <= food_grams < 400:
        group3 += 1

    total_grams += food_grams

price_per_day = (total_grams / 1000) * FOOD_PRICE_PER_1KG

print(f"Group 1: {group1} cats.")
print(f"Group 2: {group2} cats.")
print(f"Group 3: {group3} cats.")


print(f"Price for food per day: {price_per_day:.2f} lv.")

