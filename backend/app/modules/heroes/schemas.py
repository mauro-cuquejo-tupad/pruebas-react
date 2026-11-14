from typing_extensions import List
from sqlmodel import SQLModel
from typing_extensions import Optional
from pydantic import ConfigDict, BaseModel, Field
from app.modules.weapons.schemas import WeaponRead

class HeroBase(SQLModel):
    model_config = ConfigDict(from_attributes=True)

    name: str = Field(..., min_lengt=1)
    secret_name: str
    age: Optional[int] = None

# requests
class HeroCreate(HeroBase):
    team_id: Optional[int] = None
    weapon_id: Optional[int] = None

class HeroUpdate(SQLModel):
    model_config = ConfigDict(from_attributes=True)

    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
    team_id: Optional[int] = None
    weapon_id: Optional[int] = None

# responses
class HeroRead(HeroBase):
    id: int    
    team_id: Optional[int] = None
    weapon_id: Optional[int] = None
    
class TeamBasicRead(BaseModel):
    # Schema reducido de team para evitar imports circulares
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    headquarters: str

class HeroReadFull(HeroRead):
    weapon: Optional[WeaponRead] = None
    team: Optional[TeamBasicRead] = None
    teams: List[TeamBasicRead] = []


# Operaciones N:M
class HeroTeamAssign(SQLModel):
    model_config = ConfigDict(from_attributes=True)
    team_id: int