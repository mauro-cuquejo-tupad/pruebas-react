from app.modules.heroes.schemas import HeroCreate
from sqlmodel import select, Session
from sqlalchemy.orm import selectinload
from app.modules.heroes.models import Hero
from typing_extensions import List, Optional


def create(session: Session, hero: HeroCreate):
    db_hero = Hero.model_validate(hero)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero

def get_heroes(session: Session) -> List[Hero]:
    statement = select(Hero).options(
        selectinload(Hero.weapon),
        selectinload(Hero.team),
    )
    return list(session.exec(statement).all())

def find_by_id(session: Session, hero_id: int) -> Optional[Hero]:
    statement = (
    select(Hero)
    .where(Hero.id == hero_id)
    .options(
        selectinload(Hero.weapon),
        selectinload(Hero.team)
        )
    )

    return session.exec(statement).first()

def update_hero():
    pass