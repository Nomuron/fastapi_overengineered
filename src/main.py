from fastapi import FastAPI
from routes.practice import practice_router

app = FastAPI()

app.include_router(practice_router, prefix="/practice")

@app.get("/")
def read_root():
    return {"message": "Hello World"}