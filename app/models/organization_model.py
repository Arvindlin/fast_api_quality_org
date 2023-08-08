import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer, Boolean, UUID, Text
from sqlalchemy.dialects.mysql import CHAR
from app.models.model import Base
import datetime


class Organization(Base):
    """
    Table to identify the organization.
    """
    __tablename__ = "organizations"
    __table_args__ = {"schema": "md_wqms_mock"}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    organization_name = Column(String(250))
    organization_pic = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    log = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    # updated_at = Column(DateTime, nullable=True)
    # deleted_at = Column(DateTime, nullable=True)


class Organization_level_2(Base):
    """
        Table for level 2 organization
    """
    __tablename__ = "organizations_level2"
    __table_args__ = {"schema": "md_wqms_mock"}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    organization_id = Column(Integer, ForeignKey('md_wqms_mock.organizations.id'), index=True)
    level1_id = Column(Integer, ForeignKey('md_wqms_mock.organizations.id'), index=True)
    level_name = Column(String(250))
    is_active = Column(Boolean, default=True)
    log = Column(Text, nullable=True)
    audit_sheet_creation = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.now)


class Organization_level_3(Base):
    """
        Table for level 3 organization
    """
    __tablename__ = "organizations_level_3"
    __table_args__ = {"schema": "md_wqms_mock"}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    organization_id = Column(Integer, ForeignKey('md_wqms_mock.organizations.id'), index=True)
    level2_id = Column(Integer, ForeignKey('md_wqms_mock.organizations_level2.id'), index=True)
    level_name = Column(String(250))
    is_active = Column(Boolean, default=True)
    log = Column(Text, nullable=True)
    audit_sheet_creation = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.now)


class Organization_level_4(Base):
    """
        Table for level 4 organization
    """
    __tablename__ = "organizations_level_4"
    __table_args__ = {"schema": "md_wqms_mock"}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    organization_id = Column(Integer, ForeignKey('md_wqms_mock.organizations.id'), index=True)
    level3_id = Column(Integer, ForeignKey('md_wqms_mock.organizations_level_3.id'), index=True)
    level_name = Column(String(250))
    is_active = Column(Boolean, default=True)
    log = Column(Text, nullable=True)
    audit_sheet_creation = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.now)


class Organization_level_5(Base):
    """
        Table for level 5 organization
    """
    __tablename__ = "organizations_level_5"
    __table_args__ = {"schema": "md_wqms_mock"}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    organization_id = Column(Integer, ForeignKey('md_wqms_mock.organizations.id'), index=True)
    level4_id = Column(Integer, ForeignKey('md_wqms_mock.organizations_level_4.id'), index=True)
    level_name = Column(String(250))
    is_active = Column(Boolean, default=True)
    log = Column(Text, nullable=True)
    audit_sheet_creation = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.now)



