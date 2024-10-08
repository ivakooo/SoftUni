num = int(input())

for i in range(1, num + 1):
    sum_of_digits = 0
    single_digit = i
    while single_digit > 0:
        sum_of_digits += single_digit % 10
        single_digit = (single_digit // 10)
    if str(sum_of_digits) in ["5", "7", "11"]:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")