locations = int(input())

for i in range(locations):
    expected_mining_per_day = float(input())
    number_of_days_on_location = int(input())

    total_gold = 0

    for j in range(number_of_days_on_location):
        mined_gold = float(input())
        total_gold += mined_gold

    average_mining_per_day = total_gold / number_of_days_on_location

    difference = abs(average_mining_per_day - expected_mining_per_day)

    if average_mining_per_day >= expected_mining_per_day:
        print(f"Good job! Average gold per day: {average_mining_per_day:.2f}.")
    else:
        print(f"You need {difference:.2f} gold.")

a`