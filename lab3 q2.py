marks = int(input("Enter your marks: "))

if 88 <= marks <= 100:
    print("Grade: A\nGrade Point: 4.0")

elif 80 <= marks <= 87:
    print("Grade: A-\nGrade Point: 3.7")

elif 75 <= marks <= 79 :
    print("Grade: B+\nGrade Point: 3.4")

elif 70 <= marks <= 74 :
    print("Grade: B\nGrade Point: 3.0")

elif 67 <= marks <= 69 :
    print("Grade: B-\nGrade Point: 2.7")

elif 64 <= marks <= 66 :
    print("Grade: C+\nGrade Point: 2.4")

elif 60 <= marks <= 63 :
    print("Grade: C\nGrade Point: 2.0")

elif 57 <= marks <= 59 :
    print("Grade: C-\nGrade Point: 1.7")

elif 54 <= marks <= 56 :
    print("Grade: D+\nGrade Point: 1.4")

elif 50 <= marks <= 53 :
    print("Grade: D\nGrade Point: 1.0")

else:
    print("Marks too low/invalid.")
