from fastapi import FastAPI

from app.service import add, divide

app = FastAPI(title="CI/CD Calc API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/add")
def add_endpoint (a: float, b: float):
    return {"result": add(a, b)}

@app.get("/divide")
def divide_endpoint (a: float, b: float):
    return {"result": divide(a, b)}