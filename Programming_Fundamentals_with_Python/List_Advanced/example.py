x = [num for num in range(5)]
print(x)

nums = [1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(nums)
print(squares)

nums = [1, 2, 3, 4, 5, 6]
evens = [num for num in nums if num % 2 == 0]
print(nums)
print(evens)

nums = [1, 2, 3, 4, 5, 6]
filtered = [True if x % 2 == 0 else False for x in nums]
print(nums)
print(filtered)

my_list = [1, 2, 3, 5]
print(my_list)

my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)

my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)

my_list = [1, 2, 3]
my_list.clear()
print(my_list)

my_list = [1, 2, 3]
my_list.pop(0)
print(my_list)

my_list = [1, 2, 3]
my_list.remove(1)
print(my_list)

numbers_list = [6, 2, 1, 4, 3, 5]
sorted_numbers = sorted(numbers_list)
print(sorted_numbers)

numbers_list = [6, 2, 1, 4, 3, 5]
sorted_numbers = sorted(numbers_list, key=lambda x: -x)
print(sorted_numbers)

strings_list = ["1", "2", "3", "4"]
numbers_list = list(map(int, strings_list))  # [1, 2, 3, 4]
print(numbers_list)

numbers_list = [1, 2, 3, 4]
doubled_list = list(map(lambda x: x * 2, numbers_list))
print(doubled_list)

numbers_list = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers_list))
print(even_numbers)

nums = [1, 2, 3]
nums[0], nums[1], nums[2] = nums[2], nums[0], nums[1]
print(nums)

nums_list_1 = [1, 2, 3]
nums_list_2 = [4, 5, 6]
final_list = nums_list_1 + nums_list_2
print(final_list)

numbers = [1, 2, 2, 3, 1, 4, 5, 4]
unique_numbers = list(set(numbers))
print(unique_numbers)

from functools import reduce

list = [1, 3, 5, 6, 2]
sum = reduce(lambda a, b: a + b, list)  # 17
max = reduce(lambda a, b: a if a > b else b, list)
print(sum, max)

