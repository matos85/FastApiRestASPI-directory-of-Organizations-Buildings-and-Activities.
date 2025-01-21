import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session  # Импортируем Session
from app.models import Base, Organization, Building, Activity
from app.schemas import OrganizationCreate, BuildingCreate, ActivityCreate

# Получаем URL базы данных из переменных окружения
DATABASE_URL = os.getenv("DATABASE_URL")

# Создаем движок SQLAlchemy
engine = create_engine(DATABASE_URL)

# Создаем сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_data(db: Session):
    # Создание зданий
    buildings = [
        BuildingCreate(address="г. Москва, ул. Ленина 1, офис 3", coordinates="55.7558, 37.6173"),
        BuildingCreate(address="г. Москва, ул. Пушкина, дом 10", coordinates="55.7558, 37.6173"),
        BuildingCreate(address="г. Санкт-Петербург, Невский пр., 1", coordinates="59.9343, 30.3351"),
        BuildingCreate(address="г. Казань, ул. Баумана, 1", coordinates="55.8304, 49.0661"),
        BuildingCreate(address="г. Екатеринбург, ул. Ленина, 1", coordinates="56.8389, 60.6056"),
        BuildingCreate(address="г. Новосибирск, Красный проспект, 1", coordinates="55.0084, 82.9357"),
        BuildingCreate(address="г. Нижний Новгород, ул. Минина, 1", coordinates="56.3269, 44.0059"),
        BuildingCreate(address="г. Челябинск, ул. Труда, 1", coordinates="55.1644, 61.4368"),
        BuildingCreate(address="г. Омск, ул. Ленина, 1", coordinates="54.9920, 73.3686"),
        BuildingCreate(address="г. Ростов-на-Дону, ул. Седина, 1", coordinates="47.2225, 39.7188"),
    ]

    for building in buildings:
        db.add(Building(**building.dict()))

    db.commit()

    # Создание видов деятельности
    activities = [
        ActivityCreate(name="Еда"),
        ActivityCreate(name="Автомобили"),
        ActivityCreate(name="Легковые"),
        ActivityCreate(name="Торговля"),
        ActivityCreate(name="Услуги"),
        ActivityCreate(name="Производство"),
        ActivityCreate(name="Строительство"),
        ActivityCreate(name="Транспорт"),
        ActivityCreate(name="Образование"),
        ActivityCreate(name="Здравоохранение"),
    ]

    for activity in activities:
        db.add(Activity(**activity.dict()))

    db.commit()



    # Создание организаций
    organizations = [
        OrganizationCreate(
            name="ООО 'Рога и Копыта'",
            phone_numbers=["2-222-222", "3-333-333", "8-923-666-13-13"],
            building_id=1,  # ID первого здания
            activities=[1, 2]  # ID видов деятельности
        ),
        OrganizationCreate(
            name="ЗАО 'Молочная продукция'",
            phone_numbers=["1-111-111", "2-222-222"],
            building_id=2,
            activities=[1]
        ),
        OrganizationCreate(
            name="ИП 'Светлый путь'",
            phone_numbers=["8-800-555-35-35"],
            building_id=3,
            activities=[2, 3]
        ),
        OrganizationCreate(
            name="ООО 'Строитель'",
            phone_numbers=["4-444-444"],
            building_id=4,
            activities=[6, 7]
        ),
        OrganizationCreate(
            name="ЗАО 'Торговая сеть'",
            phone_numbers=["5-555-555"],
            building_id=5,
            activities=[4]
        ),
        OrganizationCreate(
            name="ООО 'Образовательные услуги'",
            phone_numbers=["6-666-666"],
            building_id=6,
            activities=[9]
        ),
        OrganizationCreate(
            name="ИП 'Здоровье'",
            phone_numbers=["7-777-777"],
            building_id=7,
            activities=[10]
        ),
        OrganizationCreate(
            name="ООО 'Транспортные услуги'",
            phone_numbers=["8-888-888"],
            building_id=8,
            activities=[8]
        ),
        OrganizationCreate(
            name="ЗАО 'Производственные мощности'",
            phone_numbers=["9-999-999"],
            building_id=9,
            activities=[5]
        ),
        OrganizationCreate(
            name="ООО 'Автомобильный сервис'",
            phone_numbers=["1-234-567"],
            building_id=10,
            activities=[2]
        ),
    ]

    for organization in organizations:
        db.add(Organization(**organization.dict()))

    db.commit()


def main():
    # Создаем все таблицы в базе данных
    Base.metadata.create_all(bind=engine)

    # Получаем сессию базы данных
    db: Session = SessionLocal()

    try:
        # Инициализируем данные
        init_data(db)
        print("Данные успешно инициализированы!")
    except Exception as e:
        print(f"Произошла ошибка при инициализации данных: {e}")
    finally:
        db.close()  # Закрываем сессию


if __name__ == "main":
    main()