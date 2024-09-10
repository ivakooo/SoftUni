needed_food_in_kg = int(input())

total_grams = 0

while True:
    grams = input()
    if grams == "Adopted":
        break

    total_grams += int(grams)

needed_food_in_grams = needed_food_in_kg * 1000
difference = abs(total_grams - needed_food_in_grams)

if needed_food_in_grams >= total_grams:
    print(f"Food is enough! Leftovers: {difference} grams." )
else:
    print(f"Food is not enough. You need {difference} grams more.")