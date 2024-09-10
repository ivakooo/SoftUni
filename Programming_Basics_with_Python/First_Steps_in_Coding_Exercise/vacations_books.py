number_of_pages = int(input())
pages_per_hour = int(input())
days_for_reading = int(input())

total_time_for_reading = number_of_pages // pages_per_hour
hours_for_reading_per_day = total_time_for_reading / days_for_reading

print(hours_for_reading_per_day)


