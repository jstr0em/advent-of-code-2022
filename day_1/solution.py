with open("input.txt", "r") as f:
    calories = f.read().splitlines() 

elf_calories = {}
elf = 0

for calorie in calories:
    if calorie != "":
        try:
            elf_calories[elf] += int(calorie)
        except:
            elf_calories[elf] = int(calorie)
    else:
        elf += 1

sorted_elf_dict = sorted(elf_calories.items(), key=lambda x: x[1], reverse=True)

def sum_elf_calories(elf_calories, num_elves):
    total_calories = 0
    for i in range(0, num_elves):
        total_calories += elf_calories[i][1]
    return total_calories

elf_with_most_calories = sum_elf_calories(sorted_elf_dict, 1)
combined_top_3_elf_calories = sum_elf_calories(sorted_elf_dict, 3)

print(elf_with_most_calories)
print(combined_top_3_elf_calories)