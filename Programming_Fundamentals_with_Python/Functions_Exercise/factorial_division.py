def calculate_factorial(number: int) -> int:
    for multiply_number in range(1, number):
        number *= multiply_number
    return number


first_number = int(input())
second_number = int(input())
first_factorail = calculate_factorial(first_number)
second_factorail = calculate_factorial(second_number)
result = first_factorail / second_factorail
print(f"{result:.2f}")




