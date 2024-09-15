import sqlite3
from sqlalchemy import Column, Integer, String, insert, delete, update
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, Session, sessionmaker
from pydantic import BaseModel

class Item(BaseModel):
    id:int
    todo:str

#crate read update delete
Base = declarative_base()


class TODO_list(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, auto_increment=True)
    todo = Column(String)

def create_todo_list(engine:Engine)-> "TODO_list":
    todo = TODO_list()
    Base.metadata.create_all(engine,checkfirst=True)
    return todo
