from typing import List, Optional

from pydantic import BaseModel, EmailStr
from pydantic.types import constr
from app.schemas.validation import Validation

class Org_level_1(BaseModel):
    organization_name: constr(strict=True)
    organization_pic: Optional[str]
    is_active: Optional[bool]

    class Config:
        orm_mode = True


class Level(BaseModel):
    level: constr(strict=True)

    class Config:
        orm_mode = True


class Org_level_2(BaseModel):
    organization_id: int
    level1_id: int
    level_name: constr(strict=True)
    is_active: Optional[bool]

    class Config:
        orm_mode = True


class Org_update_levels(BaseModel):
    level_name: constr(strict=True)
    is_active: Optional[bool]

    class Config:
        orm_mode = True


class Org_level_3(BaseModel):
    organization_id: int
    level2_id: int
    level_name: constr(strict=True)
    is_active: Optional[bool]

    class Config:
        orm_mode = True


class Org_level_4(BaseModel):
    organization_id: int
    level3_id: int
    level_name: constr(strict=True)
    is_active: Optional[bool]

    class Config:
        orm_mode = True


class Org_level_5(BaseModel):
    organization_id: int
    level4_id: int
    level_name: constr(strict=True)
    is_active: Optional[bool]

    class Config:
        orm_mode = True