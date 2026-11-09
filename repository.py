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
