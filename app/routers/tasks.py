from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database
from .auth import oauth2_scheme
from typing import List


router = APIRouter()


@router.get("/tasks", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db), token: str = Depends(oauth2_scheme)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks


@router.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db), token: str = Depends(oauth2_scheme)):
    user = crud.get_user_by_email(db, email=token)
    return crud.create_task(db=db, task=task, user_id=user.id)
