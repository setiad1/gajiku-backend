from sqlalchemy import Column, TEXT, ForeignKey, String, Integer, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base


class User(Base):
    __tablename__ = "tbl_user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    name = Column(String(50), nullable=False, index=True)
    group_id = Column(Integer, ForeignKey('ref_group.id'), server_default="4", index=True)
    # client_id = Column(Integer, ForeignKey('tbl_client.id'), index=True)

    id_type = Column(Integer, ForeignKey('ref_id_type.id'), index=True)
    id_number = Column(String(50), index=True)
    phone = Column(String(15))
    address = Column(TEXT)

    status = Column(Enum('enabled', 'disabled'), nullable=False, server_default='disabled', index=True)
    creator = Column(Integer)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    editor = Column(Integer)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    ref_group = relationship('RefGroup', backref='tbl_user')
    ref_id_type = relationship('RefIdType', backref='tbl_user')
    ref_project = relationship('Project', backref='tbl_user')
