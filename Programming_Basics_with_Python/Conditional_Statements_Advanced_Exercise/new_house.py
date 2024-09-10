flower_type = input()
flower_count = int(input())
budget = int(input())

ROSE_PRICE = 5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

total_price = 0

if flower_type == "Roses":
    total_price = flower_count * ROSE_PRICE
    if flower_count > 80:
        total_price = total_price * 0.9

elif flower_type == "Dahlias":
    total_price = flower_count * DAHLIAS_PRICE
    if flower_count > 90:
        total_price = total_price * 0.85

elif flower_type == "Tulips":
    total_price = flower_count * TULIPS_PRICE
    if flower_count > 80:
        total_price = total_price * 0.85

elif flower_type == "Narcissus":
    total_price = flower_count * NARCISSUS_PRICE
    if flower_count < 120:
        total_price = total_price * 1.15

elif flower_type == "Gladiolus":
    total_price = flower_count * GLADIOLUS_PRICE
    if flower_count < 80:
        total_price = total_price * 1.20

difference = abs(total_price - budget)

if budget >= total_price:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")