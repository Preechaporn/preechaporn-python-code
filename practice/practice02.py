students = {}

def add_student(sid, name, age, gpa) :
    students[sid] = {"name":name , "age":age , "gpa":gpa }
    print(f"Add student {name} is success")

def update_student(sid, name=None, age=None, gpa=None) :
    if sid in students:
        if name is not None:
            students[sid][name] = name
        if age is not None:
            students[sid][age] = age
        if gpa is not None:
            students[sid][gpa] = gpa
    else:
        print(f"Student id {sid} was not found")

def delete_student(sid):
    if sid in students:
        students.pop(sid)
        print(f"student {sid} has been delete")
    else:
        print(f"student {sid} doesn't exit")

def search_student(sid):
    if sid in students:
        print(f"data of {sid} = {list(students[sid].values())}")
    else :
        print(f"student {sid} doesn't exit")

def show_all():
    if not students:
        print("don't have students data yet")
    else :
        for sid,info in students.items():
            print(f"student ID : {sid} name : {(info["name"])} age : {(info["age"])} gpa : {(info["gpa"])}")


add_student(1000,"pond",20,3.50)
add_student(1001,"pup",20,4.00)
show_all()
search_student(1001)
search_student(1000)
delete_student(1000)
show_all()
delete_student(1001)
show_all()
