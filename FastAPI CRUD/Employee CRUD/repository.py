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
def update_emp(emp_id:str, updated_emp: Employee):
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