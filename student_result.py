
num_students = int(input("Enter number of students: "))

for i in range(num_students):
    print("\nStudent", i + 1)

    name = input("Enter name: ")

    subject1 = int(input("Enter marks for subject 1: "))
    subject2 = int(input("Enter marks for subject 2: "))
    subject3 = int(input("Enter marks for subject 3: "))

    total = subject1 + subject2 + subject3
    average = total / 3

    if average >= 80:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"

    print("\nResult")
    print("Name:", name)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)