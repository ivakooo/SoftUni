import sys
from sys import maxsize

number = int(input())

max_number = -maxsize
min_number = maxsize

for _ in range(number):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number

    if current_number < min_number:
        min_number = current_number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')

"""import sys
max_number = -sys.maxsize
min_number = sys.maxsize
number_of_lines = int(input())

for _ in range(number_of_lines):
    num = int(input())
    if num > max_number:
        max_number = num
    if num < min_number:
        min_number = num
print(f"Max number: {max_number}\nMin number: {min_number}")"""

