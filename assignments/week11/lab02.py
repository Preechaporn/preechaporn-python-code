"""
Create a grade processing system with the following requirements:

A global variable passing_grade = 50

(1) A function input_students(num_students) that:

- Creates and returns a list of dictionaries
- Each dictionary contains: {'name': str, 'scores': [list of 3 scores]}

(2) A function calculate_averages(students) that:

- Uses nested loops to calculate each student's average
- Adds an 'average' key to each student dictionary
- Modifies the original list (demonstrate list mutability)

(3) A function display_results(students) that:

- Loops through students
- Uses the global passing_grade to determine pass/fail
- Prints each student's name, average, and status (PASS/FAIL)
"""

passing_grade = 50

def input_students(num_students):
    students = {}
    i = 1
    while i <= num_students:
        name = input("Enter student name: ")
        j = 1
        scorelist = []
        while j <= 3:
            score = int(input(f"Enter score {j}: "))
            scorelist.append(score)
            j += 1
        students[name] = scorelist
        i += 1
    return students

def calculate_averages(students):
    for name, scorev in students.items():
        sum_stu = 0
        for score in scorev: 
            sum_stu += score
        avg = sum_stu / len(scorev)
        students[name] = {"scores": scorev, "avg": avg}
    return students

def display_results(students):
    i = 1
    for name, value in students.items():
        if value["avg"] >= passing_grade:
            value["status"] = "PASS"
        else:
            value["status"] = "FAIL"

    for name, value in students.items():
        print(f"{i}. {name} average: {value['avg']:.2f} status: {value['status']}")
        i += 1


students = input_students(2)
students = calculate_averages(students)
display_results(students)