from math import ceil

person = int(input())
capacity = int(input())

courses = ceil(person / capacity)
print(courses)
