from pydantic import BaseModel
from datetime import date


class Employee(BaseModel):
    id: int
    name: str
    role: str
    salary: float


class TerminateRequest(BaseModel):
    effective_date: date


class TerminateResponse(BaseModel):
    id: int
    name: str
    role: str
    salary: float
    status: str
    effective_date: date