study_hours = [
    [1, 2, 1.5, 0.5, 3],
    [2.5, 0.2, 1.5, 3, 1],
    [1.5, 1, 0.5, 2, 0.5]
]

max_hours = study_hours[0][0]

names = ["Mok", "Peach", "Kian"]

for i in range(len(study_hours)):
    print(names[i], "study hours:", study_hours[i])

    total = 0
    for j in range(len(study_hours[i])):
        total += study_hours[i][j]

        if study_hours[i][j] > max_hours:
            max_hours = study_hours[i][j]

    average = total / len(study_hours[i])

    print("  Total Study Hours:", total)
    print("  Average Study Hours:", average)
    print()

print("Highest study hour recorded in the dataset:", max_hours)

"""

Using a 2D array made it easier to organize the study hours because each row represented one student’s daily study time. 
The array allowed me to use loops to calculate totals and averages efficiently without repeating code. Calculating the 
total study hours was easy since I only needed to add the values in each row. Finding the maximum value required more 
attention because each value had to be compared individually.

"""