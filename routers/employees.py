from fastapi import APIRouter, HTTPException
from models.employee import Employee, EmployeeCreate
from store.Data import employees

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.get("/")
def get_employees():
    return employees


@router.get("/{emp_id}")
def get_employee(emp_id: int):
    for emp in employees:
        if emp.id == emp_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")


@router.post("/")
def create_employee(emp: EmployeeCreate):
    new_id = max((e.id for e in employees), default=0) + 1
    new_emp = Employee(id=new_id, **emp.model_dump())
    for e in employees:
        if e.name == new_emp.name:
            raise HTTPException(status_code=400, detail="Employee already exists")
    employees.append(new_emp)
    return {"message": "Employee created", "employee": new_emp}


@router.put("/{emp_id}")
def update_employee(emp_id: int, updated_emp: Employee):
    for i, emp in enumerate(employees):
        if emp.id == emp_id:
            employees[i] = updated_emp
            return {"message": "Employee updated", "employee": updated_emp}
    raise HTTPException(status_code=404, detail="Employee not found")


@router.delete("/{emp_id}")
def delete_employee(emp_id: int):
    for i, emp in enumerate(employees):
        if emp.id == emp_id:
            deleted = employees.pop(i)
            return {"message": "Employee deleted", "employee": deleted}
    raise HTTPException(status_code=404, detail="Employee not found")
