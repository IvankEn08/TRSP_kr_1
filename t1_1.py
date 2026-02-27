from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app1 = FastAPI()

@app1.get("/")
def read_root():
    logger.info("Handling request to root endpoint")
    return {"message": "Авторелоад действительно работает"}

# uvicorn t1_1:app1 --reload --port 8001
