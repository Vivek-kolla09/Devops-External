from fastapi import FastAPI
<<<<<<< HEAD
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
=======
from fastapi import HTTPException
from model import Employee
import repository

app = FastAPI()

# details = []

# Home
@app.get("/")
def home():
    return {"message": "Welcome to the Employee CRUD Application!"}

# CREATE
@app.post("/employee")
def create_emp(employee:Employee):
    result = repository.create_emp(employee)
    if result is not None:
        return {
            "message": "Employee created successfully!",
            "employee": result
        }
    raise HTTPException(
        status_code=404,
        detail="Employee not found!"
    )
    # return {"message": "Employee not found!"}

# READ 
@app.get("/employee")
def get_emp():
    result = repository.get_emp()
    if result is not None:
        return{
            "message": "Employee fetched successfully!",
            "employee": result
        }
    raise HTTPException(
        status_code=404,
        detail="Employee not found!"
    )
    # return {"message": "Employee not found!"}

# UPDATE
@app.put("/employee/{emp_id}")
def update_emp(emp_id: int, employee: Employee):
    result = repository.update_emp(emp_id,employee)
    if result is not None:
        return{
            "message": "Employee updated successfully!",
            "employee": result
        }
    raise HTTPException(
        status_code=404,
        detail="Employee not found!"
    )
    # return {"message": "Employee not found!"}

# DELETE
@app.delete("/employee/{name}")
def delete_emp(name:str):
    result = repository.delete_emp(name)
    if result is not None:
        return{
            "message": "Employee deleted successfully!",
            "employee": result
        }
    raise HTTPException(
        status_code=404,
        detail="Employee not found!"
    )
    # return {"message": "Employee not found!"}
>>>>>>> 55296e6734301426fea2a4b8ffd6e3bc88fc8090
