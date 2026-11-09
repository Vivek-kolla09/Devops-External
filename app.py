from fastapi import FastAPI
from model import Student
import repository
app = FastAPI()

students = []

@app.get("/")
def home():
    return {"message": "FastAPI Server successfully established!"}

# CREATE LOGIC
@app.post("/students")
def create_students(student:Student):
    result = repository.create_student(student)
    if result:
        return {
            "message": "Student created successfully!",
            "student": result
        }
    return {"message": "Student not found!"}

# READ LOGIC
@app.get("/students")
def get_students():
    return {"student": repository.get_students()}

# UPDATE LOGIC
@app.put("/students/{old_name}")
def update_students(old_name:str, student:Student):
    result = repository.update_student(old_name,student)
    if result:
        return {
            "message": "Student updated successfully!",
            "student": result
        }
    return {"message": "Student not found!"}

# DELETE LOGIC
@app.delete("/students/{name}")
def delete_student(name:str):
    result = repository.delete_student(name)
    if result:
        return {
            "message": "Student deleted successfully!",
            "student": result
        }
    return { "message": "Student not found!" }
