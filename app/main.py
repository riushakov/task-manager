from fastapi import FastAPI
from app.routers import auth, tasks
from app.database import engine, Base

app = FastAPI()

app.include_router(auth.router)
app.include_router(tasks.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Таск менеджер"}