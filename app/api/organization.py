from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Organization)
def create_organization(organization: schemas.OrganizationCreate, db: Session = Depends(get_db)):
    return crud.create_organization(db=db, organization=organization)

@router.get("/{organization_id}", response_model=schemas.Organization)
def read_organization(organization_id: int, db: Session = Depends(get_db)):
    db_organization = crud.get_organization(db, organization_id=organization_id)
    if db_organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_organization

@router.get("/", response_model=list[schemas.Organization])
def read_organizations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    organizations = crud.get_organizations(db, skip=skip, limit=limit)
    return organizations