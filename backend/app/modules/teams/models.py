from sqlmodel import Relationship
from sqlmodel import SQLModel, Field

class Team(SQLModel, table=True):
    id: int | None = Field(
        default=None, primary_key=True
    )
    name: str
    headquarters: str

    # 1:N - héroes cuyo team_id apunta acá
    heroes: list["Hero"] = Relationship(back_populates="team")