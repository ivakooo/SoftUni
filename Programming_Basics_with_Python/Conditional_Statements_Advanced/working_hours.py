hour = int(input())
day = input()

if day != "Sunday":
    if 10 <= hour <= 18:
        print("open")
    else:
        print("closed")
else:
    print("closed")