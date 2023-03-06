#Aidan Moxham
#Professor Eckert
#CS-175L-01
#AverageFromInput

def read_numbers(filename):
    numbers = []
    try:
        with open("numbers.txt", "r") as file:
            for line in file:
                try:
                    num = float(line.strip())
                    numbers.append(num)
                    print("I read in {:2d} number(s) Current number is: {:7.2f} Total is: {:7.2f}".format(len(numbers), num, sum(numbers)))
                except ValueError:
                    print(f"Could not convert line '{line.strip()}' to a number.")
    except IOError:
        print(f"Could not open file {filename}.")
    return numbers

def calculate_average(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return 0

def print_average(average):
    print("Average: {:7.1f}". format(average))

def main():
    numbers = read_numbers("numbers.txt")
    average = calculate_average(numbers)
    print_average(average)

if __name__=='__main__':
    main()
