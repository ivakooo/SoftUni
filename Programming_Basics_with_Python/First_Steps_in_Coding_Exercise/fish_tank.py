length = int(input())
width = int(input())
high = int(input())
percent = float(input())

aquarium_volume = length * width * high
volume_liters = aquarium_volume * 0.001
occupied_volume = percent * 0.17
needed_liters = volume_liters * (1 - 0.17)

print(needed_liters)
