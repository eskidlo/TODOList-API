import sqlite3
from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import declarative_base, sessionmaker, Session,declarative_base
from pydantic import BaseModel,  Field
from sqlalchemy import create_engine
from typing import Optional
import json 

DATABASE_URL = "sqlite:///../databases/todo.db"
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Item(BaseModel):
    id: Optional[int] = Field(default=None,primary_key = True)
    todo: str

    class Config:
        from_attributes = True 

class TODO_list(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    todo = Column(String)

def create_todo(db: Session, todo: Item) -> bool:
    answer = True
    item = TODO_list(todo=todo.todo) 
    try:
        db.add(item)
        db.commit()
    except:
        db.rollback()
        answer = False
    return answer

def read_todo(db: Session) -> None:
    all_todo = db.query(TODO_list).all()
    return all_todo

def update_todo(db:Session, id:int, new_todo:str) -> str:
    answer = True
    try:
        db.query(Item).filter(Item.id == id)
        db.commit()
    except:
        answer = False
    return answer 
    

def delete_todo(db: Session, id: int) -> bool:
    answer = True
    try:
        db.query(TODO_list).filter(TODO_list.id == id).delete()
        db.commit()
    except:
        answer = False
    return answer

# Base.metadata.create_all(bind=engine,checkfirst=True)

# with SessionLocal() as s:
#     todo_new = Item(todo="DOOOO")
#     create_todo(s,todo_new)
#     rr = read_todo(s) 
#     # print(rr)




