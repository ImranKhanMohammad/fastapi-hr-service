from fastapi import APIRouter, HTTPException
from datetime import date
from models.employee import TerminateRequest, TerminateResponse
from store.Data import employees, terminations

router = APIRouter(prefix="/employees", tags=["Terminations"])


@router.put("/{emp_id}/terminate")
def terminate_employee(emp_id: int, request: TerminateRequest):
    if request.effective_date <= date.today():
        raise HTTPException(status_code=400, detail="Effective date must be a future date")

    for emp in employees:
        if emp.id == emp_id:
            for t in terminations:
                if t.id == emp_id:
                    raise HTTPException(status_code=400, detail="Employee already terminated")

            terminated = TerminateResponse(
                id=emp.id,
                name=emp.name,
                role=emp.role,
                salary=emp.salary,
                status="terminated",
                effective_date=request.effective_date,
            )
            terminations.append(terminated)
            return {"message": "Employee terminated", "employee": terminated}

    raise HTTPException(status_code=404, detail="Employee not found")