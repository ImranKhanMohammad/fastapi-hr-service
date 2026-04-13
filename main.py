from fastapi import FastAPI
from routers import employees, terminations

app = FastAPI(title="HR API", version="1.0.0")

app.include_router(employees.router)
app.include_router(terminations.router)


@app.get("/")
def health():
    return {"status": "HR API is running"}