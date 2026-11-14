from sqlmodel import Session
from app.modules.heroes.schemas import HeroCreate, HeroRead
from app.modules.heroes import repository as repo
from fastapi.exceptions import HTTPException



def create_hero(db: Session, hero: HeroCreate):
    hero_db = repo.create(db, hero)
    return HeroRead.model_validate(hero_db)


def find_hero_by_id(db: Session, hero_id: int):
    hero_db = repo.find_by_id(db, hero_id)
    if not hero_db:
        raise HTTPException(status_code=404, detail="Hero not found")
    return HeroRead.model_validate(hero_db)