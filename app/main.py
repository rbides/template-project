from fastapi import FastAPI
from config import settings

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Hello": settings.DATABASE_URL}

