from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://menu_db:menudb@localhost:5432/menu_db")
BaseModel = declarative_base()


class LocalSession(Session):
    def __init__(self):
        super().__init__(bind=engine)


def connect_to_db():
    return LocalSession()


class MenuModel(BaseModel):
    __tablename__ = "Menu"

    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String(50), nullable=False, unique=True)
    description = Column(String(255), nullable=True, unique=False)
    submenus_count = Column(Integer, default=0)
    dishes_count = Column(Integer, default=0)

    def add_submenu_count(self, value: int):
        self.submenus_count += value

    def add_dishes_count(self, value: int):
        self.dishes_count += value

    def delete_submenu_count(self, value: int):
        self.submenus_count -= value

    def delete_dishes_count(self, value: int):
        self.dishes_count -= value


class SubmenuModel(BaseModel):
    __tablename__ = "Submenu"

    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String(50), nullable=False, unique=True)
    description = Column(String(255), nullable=True, unique=False)
    dishes_count = Column(Integer, default=0)
    menu_id = Column(UUID, ForeignKey(MenuModel.id, ondelete='CASCADE'))

    def update_dishes_count(self, value: int):
        self.dishes_count += value

    def delete_dishes_count(self, value: int):
        self.dishes_count -= value


class DishModel(BaseModel):
    __tablename__ = "Dish"

    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String(50), nullable=False, unique=True)
    description = Column(String(255), nullable=True, unique=False)
    price = Column(String)
    submenu_id = Column(UUID, ForeignKey(SubmenuModel.id, ondelete='CASCADE'))
