import sqlite3
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session,declarative_base
from pydantic import BaseModel,  Field
from sqlalchemy import create_engine
from typing import Optional

DATABASE_URL = "sqlite:///databases/todo.db"
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Item(BaseModel):
    id: Optional[int] = Field(primary_key=True)
    todo: str


class TODO_list(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    todo = Column(String)

def create_todo(db: Session, todo: str) -> bool:
    answer = True
    try:
        new_todo = Item(todo=todo)
        db.add(new_todo)
        db.commit()
    except:
        answer = False
    return answer


def read_todo(session: Session) -> None:
    all_todo = session.query(Item.todo).all
    return all_todo

def update_todo(db:Session, id:int, new_todo:str) -> bool:
    answer = True
    try:
        db.query(Item).filter(Item.id == id)
    except:
        answer = False
    return answer 
    

def delete_todo(db: Session, id: int) -> bool:
    answer = True
    try:
        db.query(Item).filter(Item.id == id).delete()
        db.commit()
    except:
        answer = False
    return answer
