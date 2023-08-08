import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer, Boolean, UniqueConstraint
from sqlalchemy.dialects.mysql import CHAR
from app.models.model import Base
import datetime


class User(Base):
    """
    Table for the Users.
    """
    __tablename__ = "users"
    __table_args__ = {"schema": "md_wqms_mock"}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    email_id = Column(String(250), index=True, nullable=False, unique=True)
    password = Column(String(100), index=True, nullable=False)
    employee_id = Column(String(250), index=True, nullable=False, unique=True)
    doj = Column(DateTime, nullable=True, default=datetime.datetime.now().date())
    # location = Column(String(250))
    # role_id = Column(String(250),ForeignKey('omid.roles.id'), index=True)
    phone_number = Column(Integer, nullable=True)
    country_code = Column(String(10), nullable=True)
    # organization_id = Column(CHAR(36), ForeignKey('omid.organizations.id'), index=True)
    super_admin = Column(Boolean, default=False)
    status = Column(Boolean, default=True)
    is_password_reset = Column(Boolean, default=False)
    password_reset_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=True, default=datetime.datetime.now)
    # updated_at = Column(DateTime, nullable=True)
    # deleted_at = Column(DateTime, nullable=True)