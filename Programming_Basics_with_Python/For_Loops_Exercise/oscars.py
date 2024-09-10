actor_name = input()
academy_points = float(input())
count_jury = int(input())

total_jury_points = 0
final_jury_points = academy_points
for i in range(1, count_jury + 1):
    jury_name = input()
    jury_points = float(input())
    total_jury_points = (len(jury_name) * jury_points) / 2
    final_jury_points += total_jury_points
    if final_jury_points >= 1250.5:
        break

if final_jury_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {final_jury_points:.1f}!")
else:
    diff = abs(final_jury_points - 1250.5)
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")