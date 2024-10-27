from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    is_active: bool

class UserCreate(UserSchema):
    password: str

class UserOut(UserSchema):
    id: int

