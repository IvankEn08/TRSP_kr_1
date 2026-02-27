from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("index.html")

# uvicorn t1_2:app --reload --port 8001