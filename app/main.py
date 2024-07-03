import logging
from fastapi import FastAPI


app = FastAPI()
logging.basicConfig(level=logging.DEBUG)

@app.get("/")
def hello_world():
    logging.debug("Entering hello_world function.")
    return "Hello World!"

