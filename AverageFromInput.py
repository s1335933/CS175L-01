#Aidan Moxham
#Professor Eckert
#CS-175L-01
#AverageFromInput

total = 0
count = 0

with open("numbers.txt", "r") as file:
    for line in file:
        num = float(line.strip())
        count += 1
        total += num
        print(f"I read in {count} number(s) Current number is: {num:.2f} Total is: {total:.2f}")

average = total / count
print(f"Average: {average:.1f}")
