numbers_as_string = input().split()
numbers_as_integers = []
for number in numbers_as_string:
    numbers_as_integers.append(int(number))

is_even = lambda x: x % 2 == 0
final_list = list(filter(is_even, numbers_as_integers))
print(final_list)
