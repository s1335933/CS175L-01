#Aidan Moxham
#CS-175L-01
#CalculateAverage

def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    return average


def determine_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade


def repeat():
    response = input("Enter 'yes' if you would like to do another calculation: ")
    if response == "yes":
        return True
    else:
        return False


# main program
while True:
    score1 = float(input("\nEnter score 1: "))
    score2 = float(input("Enter score 2: "))
    score3 = float(input("Enter score 3: "))
    score4 = float(input("Enter score 4: "))
    score5 = float(input("Enter score 5: "))

    average_score = calc_average(score1, score2, score3, score4, score5)

    print("\nScore\t\tNumeric Grade\tLetter Grade")
    print("----------------------------------------------")
    print(f"score 1:\t{score1}\t\t{determine_grade(score1)}")
    print(f"score 2:\t{score2}\t\t{determine_grade(score2)}")
    print(f"score 3:\t{score3}\t\t{determine_grade(score3)}")
    print(f"score 4:\t{score4}\t\t{determine_grade(score4)}")
    print(f"score 5:\t{score5}\t\t{determine_grade(score5)}")
    print(f"Average score:\t{average_score}\t\t{determine_grade(average_score)}\n")

    if not repeat():
        break
