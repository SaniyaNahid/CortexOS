from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr


class UserRegister(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: EmailStr
    is_active: bool
    is_verified: bool

    model_config = ConfigDict(from_attributes=True)