from pydantic import BaseModel
from typing import List, Optional

class ActivityBase(BaseModel):
    name: str

class ActivityCreate(ActivityBase):
    pass

class Activity(ActivityBase):
    id: int
    building_id: int

    class Config:
        orm_mode = True

class BuildingBase(BaseModel):
    name: str
    organization_id: int

class BuildingCreate(BuildingBase):
    pass

class Building(BuildingBase):
    id: int
    activities: List[Activity] = []

    class Config:
        orm_mode = True

class OrganizationBase(BaseModel):
    name: str
    address: str

class OrganizationCreate(OrganizationBase):
    pass

class Organization(OrganizationBase):
    id: int
    buildings: List[Building] = []

    class Config:
        orm_mode = True