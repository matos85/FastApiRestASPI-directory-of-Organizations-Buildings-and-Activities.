# app/main.py

from fastapi import FastAPI
from app.database import engine
from app.models import Base  # Импортируем базовые модели
from app.api import organization, building, activity

# Создаем экземпляр FastAPI
app = FastAPI(title="Справочник Организаций, Зданий и Деятельностей")

# Создаем таблицы в базе данных
@app.on_event("startup")
async def startup():
    # Создаем все таблицы, если они не существуют
    Base.metadata.create_all(bind=engine)

# Регистрация маршрутов
app.include_router(organization.router, prefix="/organizations", tags=["Organizations"])
app.include_router(building.router, prefix="/buildings", tags=["Buildings"])
app.include_router(activity.router, prefix="/activities", tags=["Activities"])

# Простой тестовый маршрут
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Добро пожаловать в API каталога организаций!"}