from fastapi import FastAPI
from fastapi import HTTPException
from model import Employee
import repository

app = FastAPI()

details = []

# Home
@app.get("/")
def home():
    return {"message": "Welcome to the Employee CRUD Application!"}

# CREATE
@app.post("/employee")
def create_emp(employee:Employee):
    result = repository.create_emp(employee)
    if result:
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
    if result:
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
    if result:
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
    if result:
        return{
            "message": "Employee deleted successfully!",
            "employee": result
        }
    raise HTTPException(
        status_code=404,
        detail="Employee not found!"
    )
    # return {"message": "Employee not found!"}