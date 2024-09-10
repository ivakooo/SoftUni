from math import ceil
series_name = input()
episode_duration = int(input())
break_time = int(input())

lunch_time = break_time / 8
chill_time = break_time / 4

free_time = break_time - lunch_time - chill_time
diff = ceil(abs(free_time - episode_duration))

if free_time >= episode_duration:
    print(f"You have enough time to watch {series_name} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {diff} more minutes.")