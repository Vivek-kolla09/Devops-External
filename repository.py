<<<<<<< HEAD
from model import Student

students = []

# CREATE LOGIC
def create_student(student: Student):
    students.append(student)
    return student

# READ LOGIC
def get_students():
    return students

# UPDATE LOGIC
def update_student(old_name: str, updated_student: Student):
    for student in students:
        if student.name == old_name:
            student.name = updated_student.name
            student.course = updated_student.course
            student.age = updated_student.age
            return student

    return None

# DELETE LOGIC
def delete_student(name:str):
    for student in students:
        if student.name == name:
            students.remove(student)
            return True

    return False
=======
from model import Employee

details = []

# CREATE 
def create_emp(employee:Employee):
    details.append(employee)
    return details

# READ 
def get_emp():
    return details

# UPDATE
def update_emp(emp_id:int, updated_emp: Employee):
    for detail in details:
        if detail.emp_id == emp_id:
            # detail.emp_id = updated_emp.emp_id
            detail.name = updated_emp.name
            detail.age = updated_emp.age
            detail.dept = updated_emp.dept
            detail.salary = updated_emp.salary
            return detail
    
    return None


# DELETE
def delete_emp(name:str):
    for detail in details:
        if detail.name == name:
            details.remove(detail)
            return details

    return None
>>>>>>> 55296e6734301426fea2a4b8ffd6e3bc88fc8090
