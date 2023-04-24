import datetime
from uuid import uuid4
from sqlalchemy import Column, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import declarative_base, relationship

from api.service.postgres import create_postgres_engine

Base = declarative_base()

schema = 'public'


class User(Base):
    __tablename__ = 'USERS'
    __table_args__ = {'schema': schema}

    id = Column(String, default=lambda: str(uuid4()), primary_key=True)
    name = Column(String)
    login = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)


class Application(Base):
    __tablename__ = 'APPLICATIONS'
    __table_args__ = {'schema': schema}

    id = Column(String, default=lambda: str(uuid4()), primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now)
    functionalities = relationship("Functionality", back_populates="APPLICATIONS")


class Functionality(Base):
    __tablename__ = 'FUNCTIONALITIES'
    __table_args__ = {'schema': schema}

    id = Column(String, default=lambda: str(uuid4()), primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now)
    application_id = Column(
        String,
        ForeignKey(f"{schema}.APPLICATIONS.id", ondelete="CASCADE"),
        nullable=False
    )
    APPLICATIONS = relationship("Application", back_populates="functionalities")
    LOGS = relationship("Log", back_populates="functionalities")


class Log(Base):
    __tablename__ = 'LOGS'
    __table_args__ = {'schema': schema}

    id = Column(String, default=lambda: str(uuid4()), primary_key=True)
    name = Column(String)
    dt_start_exec = Column(DateTime, default=datetime.datetime.now)
    dt_end_exec = Column(DateTime, nullable=True)
    log = Column(JSON, nullable=False)
    functionality_id = Column(
        String,
        ForeignKey(f"{schema}.FUNCTIONALITIES.id", ondelete="CASCADE"),
        nullable=False
    )
    functionalities = relationship("Functionality", back_populates="LOGS")


class Script(Base):
    __tablename__ = 'SCRIPTS'
    __table_args__ = {'schema': schema}

    id = Column(String, default=lambda: str(uuid4()), primary_key=True)
    name = Column(String)
    begin_at = Column(DateTime, default=datetime.datetime.now)


class Solicitation(Base):
    __tablename__ = 'SOLICITATIONS'
    __table_args__ = {'schema': schema}

    id = Column(String, default=lambda: str(uuid4()), primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, nullable=True)


class Status(Base):
    __tablename__ = 'STATUS'
    __table_args__ = {'schema': schema}

    id = Column(String, default=lambda: str(uuid4()), primary_key=True)
    name = Column(String)

# Base.metadata.drop_all(create_postgres_engine())
# Base.metadata.create_all(create_postgres_engine())
