from fastapi import FastAPI
from settings import settings

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/settings/{key}")
def read_setting(key: str):
    value = settings.get_attribute(key)
    if value:
        return {key: value}
    else:
        return {"error": "Key not found"}
