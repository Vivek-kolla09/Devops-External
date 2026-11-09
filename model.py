from pydantic import BaseModel

class Employee(BaseModel):
    emp_id: int
    name: str
    age: str
    dept: str
    salary: float