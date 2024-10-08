def smallest_of_three_numbers(list_of_numbers: list) -> int:
    return min(list_of_numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())
smallest_number = smallest_of_three_numbers([first_number, second_number, third_number])
print(smallest_number)
