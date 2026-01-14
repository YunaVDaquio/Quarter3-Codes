names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

total_steps = [sum(person_steps) for person_steps in steps]

max_steps = max(total_steps)
max_index = total_steps.index(max_steps)
person_max = names[max_index]

min_steps = min(total_steps)

print("Total steps per person:")
for name, total in zip(names, total_steps):
    print(f"{name}: {total} steps")

print(f"\nPerson with the highest total steps: {person_max} ({max_steps} steps)")
print(f"Difference between highest and lowest total steps: {max_steps - min_steps} steps")
