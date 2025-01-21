from sqlalchemy.orm import Session
from app import models, schemas

class OrganizationService:
    def init(self, db: Session):
        self.db = db

    def create_organization(self, organization: schemas.OrganizationCreate):
        db_organization = models.Organization(**organization.dict())
        self.db.add(db_organization)
        self.db.commit()
        self.db.refresh(db_organization)
        return db_organization

    def get_organization(self, organization_id: int):
        return self.db.query(models.Organization).filter(models.Organization.id == organization_id).first()

    def get_organizations(self, skip: int = 0, limit: int = 10):
        return self.db.query(models.Organization).offset(skip).limit(limit).all()


class BuildingService:
    def init(self, db: Session):
        self.db = db

    def create_building(self, building: schemas.BuildingCreate):
        db_building = models.Building(**building.dict())
        self.db.add(db_building)
        self.db.commit()
        self.db.refresh(db_building)
        return db_building

    def get_building(self, building_id: int):
        return self.db.query(models.Building).filter(models.Building.id == building_id).first()

    def get_buildings(self, skip: int = 0, limit: int = 10):
        return self.db.query(models.Building).offset(skip).limit(limit).all()


class ActivityService:
    def init(self, db: Session):
        self.db = db

    def create_activity(self, activity: schemas.ActivityCreate):
        db_activity = models.Activity(**activity.dict())
        self.db.add(db_activity)
        self.db.commit()
        self.db.refresh(db_activity)
        return db_activity

    def get_activity(self, activity_id: int):
        return self.db.query(models.Activity).filter(models.Activity.id == activity_id).first()

    def get_activities(self, skip: int = 0, limit: int = 10):
        return self.db.query(models.Activity).offset(skip).limit(limit).all()