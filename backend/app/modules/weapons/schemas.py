from pydantic import BaseModel, ConfigDict, Field

class WeaponBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str = Field(..., min_length = 1)

class WeaponCreate(WeaponBase):
    pass

class WeaponRead(WeaponBase):
    id: int