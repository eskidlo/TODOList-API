from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import declarative_base, sessionmaker, Session, declarative_base
from pydantic import BaseModel,  Field
from sqlalchemy import create_engine
from typing import Optional

DATABASE_URL = "sqlite:///../databases/todo.db"
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Item(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    todo: str

    class Config:
        from_attributes = True


class TODO_list(Base):
    __tablename__ = "DO"
    id = Column(Integer, primary_key=True, autoincrement=True)
    todo = Column(String)


def create_todo(db: Session, todo: Item) -> bool:
    answer = "The task has been created!"
    item = TODO_list(todo=todo.todo)
    try:
        db.add(item)
        db.commit()
    except:
        db.rollback()
        answer = "Something went wrong, the task could not be created. Try again!! :("
    return answer


def read_todo(db: Session) -> None:
    all_todo = db.query(TODO_list).all()
    return all_todo


def update_todo(db: Session, id: int, new_todo: str) -> str:
    answer = "The task has been updated!"
    check = bool(db.query(TODO_list.id).filter_by(id=id).first())
    if check:
        try:
            db.query(TODO_list).filter(TODO_list.id == id).update(
                {TODO_list.todo: new_todo})
            db.commit()
        except:
            db.rollback()
            answer = "Something went wrong, the task could not be updated. Try again!! :("
    else:
        answer = "There is no task with this id"
    return answer


def delete_todo(db: Session, id: int) -> bool:
    answer = "The task has been deleted!"
    check = bool(db.query(TODO_list.id).filter_by(id=id).first())
    if check:
        try:
            db.query(TODO_list).filter(TODO_list.id == id).delete()
            db.commit()
        except:
            answer = "Something went wrong, the task could not be deleted. Try again!! :("
    else:
        answer = "There is no task with this id"
    return answer
