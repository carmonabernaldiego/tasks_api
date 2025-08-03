from fastapi import FastAPI
from app.database import Base, engine
from app.routers import tasks
import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API", version="1.0")

app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "API is running! Go to /docs for documentation."}
