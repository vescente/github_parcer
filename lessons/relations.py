from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

engine = create_engine(
    'sqlite:///' + os.path.join(BASE_DIR, 'db', 'lesson_orm.db'), echo=True)


Base = declarative_base()

# many to many association table
association_table = Table('vacancy_skill', Base.metadata,
                          Column('id', Integer, primary_key=True),
                          Column('vacancies_id', Integer, ForeignKey('vacancies.id')),
                          Column('skill_id', Integer, ForeignKey('skill.id'))
                          )


class Region(Base):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Skill(Base):
    __tablename__ = 'skill'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Vacancies(Base):
    __tablename__ = 'vacancies'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    region_id = Column(Integer, ForeignKey('region.id'))

    def __init__(self, name, region_id):
        self.name = name
        self.region_id = region_id

    def __str__(self):
        return self.name


# Создание таблицы
Base.metadata.create_all(engine)


# Создание объекта
Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
    Region('Moscow'),
    Region('Saint-Petersburg'),
    Region('Kazan'),
    Skill('Python'),
    Skill('Django'),
    Skill('Flask'),
    Skill('SQLAlchemy'),
])

session.commit()

# создаем вакансии в разных регионах
regions = session.query(Region).all()

for region in regions:
    new_vacancy = Vacancies(f'Python Developer in {region}', region.id)
    session.add(new_vacancy)

session.commit()


# Выборка вакансий по региону
moscow_vacancies = session.query(Region).first()
print(moscow_vacancies.name)

# альтернативный вариант back populates
for vacancy in moscow_vacancies.vacancies:
    print(vacancy.name)

# session.close()