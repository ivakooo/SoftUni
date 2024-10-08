def is_palindrome(number: str) -> bool:
    return number == number[::-1]


numbers_as_string = input().split(", ")
for current_number in numbers_as_string:
    print(is_palindrome(current_number))