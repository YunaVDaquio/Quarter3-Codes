study_hours = [
    [1, 2, 1.5, 0.5, 3],     # Mok
    [2.5, 0.2, 1.5, 3, 1],   # Peach
    [1.5, 1, 0.5, 2, 0.5]    # Kian
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

most_active_day = days[0]
highest_total = 0

for day_index in range(len(days)):
    daily_total = 0

    for person_index in range(len(study_hours)):
        daily_total += study_hours[person_index][day_index]

    print(days[day_index], "total study hours:", daily_total)

    if daily_total > highest_total:
        highest_total = daily_total
        most_active_day = days[day_index]

print("\nMost active day overall:", most_active_day)
