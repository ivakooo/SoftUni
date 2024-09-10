budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_memory_count = int(input())

video_cards_price = video_cards_count * 250
processors_price = processors_count * video_cards_price * 0.35
ram_memory_price = ram_memory_count * video_cards_price * 0.1

total_price = video_cards_price + processors_price + ram_memory_price

if video_cards_count > processors_count:
    total_price = total_price - (total_price * 0.15)
else:
    total_price = total_price

difference = f"{abs(budget - total_price):.2f}"

if total_price <= budget:
    print(f"You have {difference} leva left!")
else:
    print(f"Not enough money! You need {difference} leva more!")

