import datetime
from fastapi import Depends
from sqlalchemy.orm import Session, selectinload
from app.core.models import RefGroup, RefIdType


def list_ref_group(db: Session = Depends):
    dt_ref_group = db.query(RefGroup).all()
    return dt_ref_group


def list_id_type(db: Session = Depends):
    dt_ref_id_type = db.query(RefIdType).all()
    return dt_ref_id_type


def find_id_type(s: str, db: Session = Depends):
    dt_ref_id_type = db.query(RefIdType).filter(RefIdType.id_type.like('%{0}%'.format(s))).all()
    return dt_ref_id_type

