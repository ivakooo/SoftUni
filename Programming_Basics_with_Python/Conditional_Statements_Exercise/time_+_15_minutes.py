hours = int(input())
minutes = int(input()) + 15


# minutes = minutes + 15

if minutes >= 60:
    hours += 1
    minutes -= 60
if minutes < 10:
    minutes = "0" + str(minutes)

if hours > 23:
    hours = 0

print(f"{hours}:{minutes}")

