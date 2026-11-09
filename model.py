from pydantic import BaseModel

<<<<<<< HEAD
class Student(BaseModel):
    name: str
    age: int
    course: str
=======
class Employee(BaseModel):
    emp_id: int
    name: str
    age: str
    dept: str
    salary: float
>>>>>>> 55296e6734301426fea2a4b8ffd6e3bc88fc8090
