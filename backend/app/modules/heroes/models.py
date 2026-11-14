from typing_extensions import TYPE_CHECKING
from typing_extensions import Optional
from sqlmodel import Relationship
from sqlmodel import SQLModel, Field


if TYPE_CHECKING:
    #solo para type hints: evita import circular en runtime
    from app.modules.weapons.models import Weapon
    from app.modules.teams.models import Team

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
    
    #FK 1:1 - arma asignada
    weapon_id: int | None = Field(default=None, foreign_key="weapon.id", unique=True)
    
    #FK 1:N - equipo principal
    team_id: int | None = Field(default=None, foreign_key="team.id")

    # ORM - navegación
    weapon: Optional[Weapon] = Relationship(back_populates="hero")
    team: Optional[Team] = Relationship(back_populates="heroes")