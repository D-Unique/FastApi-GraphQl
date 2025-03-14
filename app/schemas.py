from pydantic import BaseModel, SecretStr, EmailStr, field_validator
from datetime import datetime
from typing import Literal

class UserBase(BaseModel):
    """Pydentic typing for the User Endpoint """
    name: str
    email: str
    password: SecretStr
    user_type: Literal["Customer", "Admin", "Manager"]
    
    @field_validator("name")
    def validate_name(cls, value):
        if value is None:
            raise ValueError("Name is Required") 
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        return value

    @field_validator("password")
    def validate_password(cls, value):
        if value is None:
            raise ValueError("Password is Required")
        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters long.")
        return value
    


class UserCreate(UserBase):
    password: str

class UserGetResponse(UserBase):
    name: str
    email: EmailStr
    created_at: datetime

class UserPostResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
