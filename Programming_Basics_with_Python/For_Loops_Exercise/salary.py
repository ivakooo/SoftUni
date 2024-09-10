tabs = int(input())
salary = int(input())

for i in range(1, tabs + 1):
    site = input()
    if site == "Facebook":
        salary -= 150
    elif site == "Instagram":
        salary -= 100
    elif site == "reddit":
        salary -= 50

    if salary <= 0:
        break

if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")