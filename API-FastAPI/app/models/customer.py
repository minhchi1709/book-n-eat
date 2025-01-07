from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import date, datetime

class Customer(SQLModel, table=True):
    id: int | None = Field(None, primary_key=True)
    email: str = Field(index = True, unique = True)
    firstname: str
    lastname: str
    birthday: date
    createdAt: datetime