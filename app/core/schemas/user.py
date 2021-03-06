import datetime
from pydantic import BaseModel
from typing import Optional


class ResponseData(BaseModel):
    data: str


class User(BaseModel):
    email: Optional[str]
    address: Optional[str]
    name: Optional[str]
    status: Optional[str]
    group_id: Optional[int]
    creator: Optional[int]
    # project_id: Optional[int]
    created_at: Optional[datetime.datetime]
    id_type: Optional[int]
    editor: Optional[int]
    username: Optional[str]
    id_number: Optional[str]
    updated_at: Optional[datetime.datetime]
    id: Optional[int]
    phone: Optional[str]
    # password: Optional[str]

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class UserLoginOut(BaseModel):
    access_token: str
    token_type: str


class UserRegister(BaseModel):
    name: str
    username: str
    password: str
    email: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    email: Optional[str]
    name: Optional[str]
    id_type: Optional[int]
    id_number: Optional[int]
    phone: Optional[str]
    address: Optional[str]

    class Config:
        orm_mode = True


class GroupUpdate(BaseModel):
    group_id: int

    class Config:
        orm_mode = True


class UpdatePassword(BaseModel):
    old_password: str
    new_password: str
    confirm_new_password: str

    class Config:
        orm_mode = True


class Activation(BaseModel):
    acticode: str

    class Config:
        orm_mode = True


class FindUserByUsername(BaseModel):
    username: str

    class Config:
        orm_mode = True


class UserGroup(BaseModel):
    id: Optional[str]
    group_description: Optional[str]
    group_name: Optional[str]

    class Config:
        orm_mode = True


class UserIdType(BaseModel):
    id: Optional[int]
    id_type: Optional[str]
    id_description: Optional[str]

    class Config:
        orm_mode = True


class UserProject(BaseModel):
    id: Optional[int]
    project: Optional[str]
    token: Optional[str]
    address: Optional[str]
    responsible_name: Optional[str]
    responsible_id_type: Optional[int]
    responsible_id_number: Optional[str]
    user_id: Optional[int]
    creator: Optional[int]
    created_at: Optional[datetime.datetime]
    editor: Optional[int]
    updated_at: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class UserDetailOut(User):
    ref_group: UserGroup
    ref_id_type: Optional[UserIdType]
    ref_project: Optional[list[UserProject]]

    class Config:
        orm_mode = True


class RegisterProject(BaseModel):
    project: str
    address: str
    responsible_name: str
    responsible_id_type: int
    responsible_id_number: str

    class Config:
        orm_mode = True



