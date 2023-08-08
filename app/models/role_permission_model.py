import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer, Boolean, UUID
from sqlalchemy.dialects.mysql import CHAR
from app.models.model import Base
import datetime


class Role(Base):
    """
    Table to identify the organization.
    """
    __tablename__ = "roles"
    __table_args__ = {"schema": "md_wqms_mock"}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    role_name = Column(String(250))
    organization_id = Column(Integer, ForeignKey('md_wqms_mock.organizations.id'), index=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    # updated_at = Column(DateTime, nullable=True)
    # deleted_at = Column(DateTime, nullable=True)


class Permission(Base):
    """
    Table to identify the permissions.
    """
    __tablename__ = "permissions"
    __table_args__ = {"schema": "md_wqms_mock"}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    role_name = Column(String(250))
    role_id = Column(Integer, ForeignKey('md_wqms_mock.roles.id'))
    created_at = Column(DateTime, default=datetime.datetime.now)
    # updated_at = Column(DateTime, nullable=True)
    # deleted_at = Column(DateTime, nullable=True)