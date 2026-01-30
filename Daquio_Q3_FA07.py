study_hours = [
    [1, 2, 1.5, 0.5, 3],
    [2.5, 0.2, 1.5, 3, 1],
    [1.5, 1, 0.5, 2, 0.5]
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
people = ["Me", "Peach", "Kian"]

for i in range(len(study_hours)):
    print(f"\nStudy hours for {people[i]}:")
    for j in range(len(days)):
        print(days[j] + ":", study_hours[i][j], "hours")

print("\n--- Totals and Averages ---")
for i in range(len(study_hours)):
    total = sum(study_hours[i])
    average = total / len(days)
    print(f"{people[i]} - Total: {total} hours, Average: {average:.2f} hours per day")

all_hours = []
for row in study_hours:
    all_hours.extend(row)

print("\nMaximum study time recorded:", max(all_hours), "hours")
print("Minimum study time recorded:", min(all_hours), "hours")
