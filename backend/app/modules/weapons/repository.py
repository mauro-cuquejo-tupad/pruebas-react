
from sqlmodel import select
from app.modules.weapons.schemas import WeaponCreate
from sqlmodel import Session
from app.modules.weapons.models import Weapon

def create(session: Session, weapon: WeaponCreate):
    db_weapon = Weapon.model_validate(weapon)
    session.add(db_weapon)
    session.commit()
    session.refresh(db_weapon)
    return db_weapon

def find_by_id(session: Session, weapon_id: int):
    statement = (select(Weapon).where(Weapon.id == weapon_id))

    db_weapon = session.exec(statement).first()
    return db_weapon