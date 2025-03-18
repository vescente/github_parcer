from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

engine = create_engine(
    'sqlite:///' + os.path.join(BASE_DIR, 'db', 'lesson_orm.db'), echo=True)


Base = declarative_base()


class Region(Base):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(Integer, nullable=True)
    note = Column(String, nullable=True)

    def __init__(self, name, number, note):
        self.name = name
        self.number = number
        self.note = note


# Создание таблицы
# Base.metadata.create_all(engine)



# Создание объекта
# region1 = Region('Moscow', 1, 'Capital of Russia')
# region2 = Region('Saint-Petersburg', 2, 'City of Russia')
# region3 = Region('Kazan', 3, 'City of Russia')


# Создание сессии
# with Session(engine) as session:
#     session.add(region1)
#     session.add(region2)
#     session.add(region3)
#     session.commit()

# Создание записей циклом
# with Session(engine) as session:
#     for i in range(10):
#         region = Region(f'Region {i+1}', i+1, f'Note {i+1}')
#         session.add(region)
#     session.commit()

# Получение всех записей без контекстного менеджера
Session = sessionmaker(bind=engine)
session = Session()
region = session.query(Region).all()

for region in region:
    print(region.id, region.name)

# session.commit()
session.close()