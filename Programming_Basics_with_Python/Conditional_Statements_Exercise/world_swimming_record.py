from math import floor

world_record = float(input())
distance = float(input())
time_in_sec_for_1m = float(input())

total_time = distance * time_in_sec_for_1m
delay_in_sec = floor(distance / 15) * 12.5

final_time = (distance * time_in_sec_for_1m) + delay_in_sec
difference = abs(world_record - final_time)

if final_time >= world_record:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {final_time:.2f} seconds.")