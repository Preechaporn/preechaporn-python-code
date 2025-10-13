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

def input_students(n):
    students = []
    for i in range(n):
        name = input("Enter students name : ")
        scores = []
        for j in range(3):
            score = int(input("Enter students scores :"))
            scores.append(score)
        students.append({"name":name,"scores":scores})
    return students

def calculate_averages(students):
    for data in students:
        sumv = 0
        n = 0
        for score in data["scores"]:
            sumv += score
            n += 1
        avg = sumv/n             # or avg = sum / len(data["scores"])
        data["average"] = avg 
    return students

def display(students):
    for data in students:
        if data["average"] >= passing_grade :
            data["status"] = "pass"
        else :
            data["status"] = "fail"
        print(f"name:{data['name']} average:{data['average']:.2f} status:{data['status']}")


n = int(input("Enter number of students: "))
students = input_students(n)
students = calculate_averages(students)
display(students)