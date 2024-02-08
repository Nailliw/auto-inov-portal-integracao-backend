from typing import List
from uuid import uuid4
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, mapped_column, Mapped

from api.service.postgres import create_postgres_engine

Base = declarative_base()

schema = 'public'

class Jobs(Base):
    """
    """
    __tablename__='job'

    id = Column(Integer, name="id", primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120))
    fullname: Mapped[str] = mapped_column(String(120))
    url: Mapped[str] = mapped_column(String(120))
    category: Mapped[List["Category"]] = relationship(back_populates="job")
    execution: Mapped[List["Execution"]] = relationship(back_populates="job")


class Category(Base):
    __tablename__='category'

    id = Column(Integer, name="id", primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120))
    job_id: Mapped[str] = mapped_column(ForeignKey("job.id"))
    job: Mapped["Jobs"] = relationship(back_populates="category")


class Execution(Base):
    __tablename__='execution'

    id = Column(Integer, name="id", primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120))
    job_id: Mapped[str] = mapped_column(ForeignKey("job.id"))
    job: Mapped["Jobs"] = relationship(back_populates="execution")

# Base.metadata.drop_all(create_postgres_engine())
# Base.metadata.create_all(create_postgres_engine())
