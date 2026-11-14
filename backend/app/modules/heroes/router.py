
from app.modules.heroes.schemas import HeroRead
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.modules.heroes.schemas import HeroCreate
from app.modules.heroes import service

router = APIRouter(prefix="/heroes", tags=["heroes"])

@router.post("/")
def create_hero(hero: HeroCreate, session: Session = Depends(get_session)) -> HeroRead:
    return service.create_hero(session, hero)

@router.get("/{hero_id}")
def find_hero_by_id(hero_id: int, session: Session = Depends(get_session)) -> HeroRead:
    return service.find_hero_by_id(session, hero_id)