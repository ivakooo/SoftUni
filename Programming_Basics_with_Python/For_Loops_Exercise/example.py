max_num = -float(input())

sum_numbers = 0
numbers = [3, 4, 1, 1, 2, 12, 1]

for num in numbers:
    sum_numbers += num
    if num > max_num:
        max_num = num


sum_others = sum_numbers - max_num


if max_num == sum_others:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = abs(max_num - sum_others)
    print("No")
    print(f"Diff = {diff}")