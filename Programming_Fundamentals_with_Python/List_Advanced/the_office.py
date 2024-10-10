happiness_scores = list(map(int, input().split()))
improvement_factor = int(input())

total_count = len(happiness_scores)

improved_happiness_scores = [score * improvement_factor for score in happiness_scores]

average_happiness = sum(improved_happiness_scores) / total_count

happy_count = len([score for score in improved_happiness_scores if score >= average_happiness])

if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
