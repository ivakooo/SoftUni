list_with_numbers = input().split()
opposite_numbers = []

for _ in list_with_numbers:
    opposite_number = -int(_)
    opposite_numbers.append(opposite_number)
print(opposite_numbers)