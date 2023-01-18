from pydantic import BaseModel, Field
# import re

# regex_price = re.compile(r"[+-]?([0-9]*[.])?[0-9]+")


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
# float = Field(dt=0)

    class Config:
        orm_mode = True
