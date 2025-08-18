students = {}

def add_student(sid, name, age, gpa) :
    students[sid] = {"name":name , "age":age , "gpa":gpa }
    print(f"Add student {name} is success")

def update_student(sid, name=None, age=None, gpa=None) :
    if sid in students:
        if name is not None:
            student[sid][name] = name
        if age is not None