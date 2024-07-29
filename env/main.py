from fastapi import FastAPI
from settings import settings

app = FastAPI()

@app.get("/value/{variable}")
def read_variable(variable: str):
    value = settings.get_attribute(variable)
    return {variable: value}

if __name__ == "_main_":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)