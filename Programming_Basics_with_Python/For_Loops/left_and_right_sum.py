"""numbers = int(input())

left_sum = 0
right_sum = 0

for i in range(numbers):
    left_sum += int(input())

for i in range(numbers):
    right_sum = right_sum + int(input())

diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {diff}")"""

numbers = int(input()) # 2

left_sum = 0
right_sum = 0

for i in range(numbers * 2):  # 0, 1, 2, 3,
    if i < numbers:
        left_sum += int(input())
    else:
        right_sum = right_sum + int(input())

diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {diff}")