from sqlalchemy.orm import Session
from . import models, schemas

def get_organization(db: Session, organization_id: int):
    return db.query(models.Organization).filter(models.Organization.id == organization_id).first()

def get_organizations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Organization).offset(skip).limit(limit).all()

def create_organization(db: Session, organization: schemas.OrganizationCreate):
    db_organization = models.Organization(**organization.dict())
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization

def get_building(db: Session, building_id: int):
    return db.query(models.Building).filter(models.Building.id == building_id).first()

def get_buildings(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Building).offset(skip).limit(limit).all()

def create_building(db: Session, building: schemas.BuildingCreate):
    db_building = models.Building(**building.dict())
    db.add(db_building)
    db.commit()
    db.refresh(db_building)
    return db_building

def get_activity(db: Session, activity_id: int):
    return db.query(models.Activity).filter(models.Activity.id == activity_id).first()

def get_activities(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Activity).offset(skip).limit(limit).all()

def create_activity(db: Session, activity: schemas.ActivityCreate):
    db_activity = models.Activity(**activity.dict())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity