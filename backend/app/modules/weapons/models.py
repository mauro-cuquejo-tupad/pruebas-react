from typing_extensions import Optional
from sqlmodel import Relationship
from sqlmodel import SQLModel, Field

class Weapon(SQLModel, table=True):
    id: int | None = Field(
        default=None, primary_key=True
    )
    name: str
    hero: Optional["Hero"] = Relationship(

        back_populates="weapon"
    )