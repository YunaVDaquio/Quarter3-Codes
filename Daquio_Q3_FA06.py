name = input("Enter student's name: ")
age = input("Enter student's age: ")
favorite_subject = input("Enter student's favorite subject: ")

student_info = {
    "Name": name,
    "Age": age,
    "Favorite Subject": favorite_subject
}

print("\n--- Student Information ---")
for key, value in student_info.items():
    print(f"{key}: {value}")
