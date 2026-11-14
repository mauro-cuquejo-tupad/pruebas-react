


from app.modules.weapons.schemas import WeaponRead
from fastapi import Depends
from fastapi import APIRouter
router = APIRouter(prefix="/weapons", tags=["weapons"])
from sqlmodel import Session
from app.core.database import get_session
from app.modules.weapons import service
from app.modules.weapons.schemas import WeaponCreate


@router.post("/")
def create_weapon(weapon: WeaponCreate, session: Session = Depends(get_session)) -> WeaponRead:
    return service.create_weapon(session, weapon)


@router.get("/{weapon_id}")
def find_weapon_by_id(weapon_id: int, session: Session = Depends(get_session)) -> WeaponRead:
    return service.find_weapon_by_id(session, weapon_id)

