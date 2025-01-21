from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Activity)
def create_activity(activity: schemas.ActivityCreate, db: Session = Depends(get_db)):
    return crud.create_activity(db=db, activity=activity)

@router.get("/{activity_id}", response_model=schemas.Activity)
def read_activity(activity_id: int, db: Session = Depends(get_db)):
    db_activity = crud.get_activity(db, activity_id=activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return db_activity

@router.get("/", response_model=list[schemas.Activity])
def read_activities(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    activities = crud.get_activities(db, skip=skip, limit=limit)
    return activities