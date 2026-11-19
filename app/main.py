import os

from fastapi import FastAPI, HTTPException

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
    try:
        return {"result": divide(a, b)}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

@app.get("/version")
def version():
    return {"version": os.getenv("APP_VERSION", "dev")}