from sqlmodel import SQLModel
from typing_extensions import List, Optional
from pydantic import Field, BaseModel, ConfigDict


# base
class TeamBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str = Field(..., min_lengt=1)
    headquarters: str

#requests
class TeamCreate(TeamBase):
    pass


class TeamUpdate(SQLModel):
    model_config = ConfigDict(from_attributes=True)
    name: Optional[str] = None
    headquarters: Optional[str] = None


# responses
class TeamRead(TeamBase):
    id: int

class HeroBasicRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    nombre: str
    secret_name: str
    age: int | None

class TeamReadFull(TeamRead):
    heroes: List[HeroBasicRead] = []

