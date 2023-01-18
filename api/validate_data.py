from pydantic import BaseModel


class MenuValidator(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True


class SubmenuValidator(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True


class DishValidator(BaseModel):
    title: str
    description: str
    price: str

    class Config:
        orm_mode = True
