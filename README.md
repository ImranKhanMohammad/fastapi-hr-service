# fastapi-hr-service

Small FastAPI HR API used as the sample target for [ai-api-automation](https://github.com/ImranKhanMohammad/ai-api-automation).

In-memory data only. Restarting the process resets employees and terminations.

## Run

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

OpenAPI: http://127.0.0.1:8000/openapi.json  
Docs: http://127.0.0.1:8000/docs

## Endpoints

| Method | Path | Body |
| --- | --- | --- |
| GET | `/employees/` | — |
| GET | `/employees/{emp_id}` | — |
| POST | `/employees/` | `name`, `role`, `salary` (server assigns `id`) |
| PUT | `/employees/{emp_id}` | full employee |
| DELETE | `/employees/{emp_id}` | — |
| PUT | `/employees/{emp_id}/terminate` | `effective_date` (must be a future date) |

Seed data: two employees, `id` 1 and 2.
