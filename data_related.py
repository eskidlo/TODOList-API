import sqlite3
from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, Session, sessionmaker
from pydantic import BaseModel

class Item(BaseModel):
    id:int
    todo:str

Base = declarative_base()

class TODO_list(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    todo = Column(String)

def create_todo_list(engine:Engine)-> "TODO_list":
    todo = TODO_list()
    Base.metadata.create_all(engine,checkfirst=True)
    return todo

def read_todo(session:any) -> None:
    pass
    
def delete_todo(session:any):
    pass

def update_todo(session:any):
    pass

def insert_todo(session:any):
    pass
