from fastapi.exceptions import HTTPException
from app.modules.weapons.schemas import WeaponRead
from sqlmodel import Session

from app.modules.weapons.schemas import WeaponCreate
from app.modules.weapons import repository as repo


def create_weapon(db:Session, weapon: WeaponCreate):
    db_weapon = repo.create(db, weapon)
    return WeaponRead.model_validate(db_weapon)


def find_weapon_by_id(db:Session, weapon_id: int):
    db_weapon = repo.find_by_id(db, weapon_id)
    if not db_weapon:
        raise HTTPException(status_code=404, detail="Weapon not found")
    return WeaponRead.model_validate(db_weapon)
    