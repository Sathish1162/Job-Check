from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "JobCheck API is running"}
