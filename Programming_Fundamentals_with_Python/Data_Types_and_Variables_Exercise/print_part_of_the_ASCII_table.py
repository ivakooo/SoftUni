start_index = int(input())
final_index = int(input())

for index in range(start_index, final_index + 1):
    if index == final_index:
        print(chr(index))
    else:
        print(chr(index), end = " ")
