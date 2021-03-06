import datetime

from pydantic import BaseModel
from typing import Optional, List, Union


class UserIdType(BaseModel):
    id: Optional[int]
    id_type: Optional[str]
    id_description: Optional[str]

    class Config:
        orm_mode = True


class SubscriptionPlan(BaseModel):
    id: Optional[int]
    plan: Optional[str]
    monthly_price: Optional[float]
    status: Optional[str]
    creator: Optional[int]
    created_at: Optional[datetime.datetime]
    editor: Optional[int]
    updated_at: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class Subscription(BaseModel):
    id: Optional[int]
    subs_plan_id: Optional[int]
    subs_month: Optional[int]
    subs_price: Optional[float]
    subs_start: Optional[datetime.datetime]
    subs_end: Optional[datetime.datetime]
    project_id: Optional[int]
    status: Optional[str]
    creator: Optional[int]
    created_at: Optional[datetime.datetime]
    editor: Optional[int]
    updated_at: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class Project(BaseModel):
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


class ProjectUpdateIn(BaseModel):
    project_id: int
    project: Optional[str]
    address: Optional[str]
    responsible_name: Optional[str]
    responsible_id_type: Optional[int]
    responsible_id_number: Optional[str]
    
    class Config:
        orm_mode = True


class ProjectDetail(BaseModel):
    project_id: int

    class Config:
        orm_mode = True


class ProjectDetailsOut(Project):
    ref_id_type: Optional[UserIdType]
    ref_subscription: Optional[list[Subscription]]

    class Config:
        orm_mode = True


class RefSubscriptionPlan(Subscription):
    ref_subscription_plan: Optional[SubscriptionPlan]


class ProjectDetailsOutV2(Project):
    ref_id_type: Optional[UserIdType]
    ref_subscription: Optional[list[RefSubscriptionPlan]]

    class Config:
        orm_mode = True


class RefSubscriptionExt(BaseModel):
    plan_id: int
    plan: str
    subs_start: datetime.datetime
    subs_end: datetime.datetime
    status: str
    subs_month: int

    class Config:
        orm_mode: True


class ProjectDetailsOutV3(Project):
    ref_id_type: Optional[UserIdType]
    ref_subscription: Optional[list[RefSubscriptionPlan]]
    ref_subscription_ext: Optional[RefSubscriptionExt]

    class Config:
        orm_mode = True


class SubscriptionDetailsOut(Subscription):
    ref_project: Optional[Project]
    ref_subscription_plan: Optional[SubscriptionPlan]

    class Config:
        orm_mode = True


class SubscriptionDetails(BaseModel):
    subscription_id: int

    class Config:
        orm_mode = True