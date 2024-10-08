def sum_numbers(first_num: int, second_num: int) -> int:
    return first_num + second_num


def subtract_numbers(result: int, third_num: int) -> int:
    return result - third_num


def add_and_subtract(first: int, second: int, third: int) -> int:
    sum_result = sum_numbers(first, second)
    final_result = subtract_numbers(sum_result, third)
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
