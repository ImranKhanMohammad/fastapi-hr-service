from models.employee import Employee, TerminateResponse

employees: list[Employee] = [
    Employee(id=1, name="Imran", role="QA", salary=50000),
    Employee(id=2, name="John", role="Developer", salary=70000),
]

terminations: list[TerminateResponse] = []
