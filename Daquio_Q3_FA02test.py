study_hours = [
    [1, 2, 1.5, 0.5, 3,], #Mok
    [2.5, 0.2, 1.5, 3, 1], #Peach
    [1.5, 1, 0.5, 2, 0.5]  #Kian
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
people = ["Me", "Peach", "Kian"]

print("Peach's study time on Wednesday:", study_hours[1][2], "hours")

print("Mok's study hours:", study_hours[0])

print("Updating Mok's Thursday study time to 2 hours.")
study_hours[0][3] = 2

print("Mok's updated study hours:", study_hours[0])