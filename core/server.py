from pydantic import BaseModel
import data_related as dr
from fastapi import FastAPI, Depends, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


def get_db():
    db = dr.SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()
templates = Jinja2Templates(directory="../templates")
dr.Base.metadata.create_all(bind=dr.engine, checkfirst=True)


@app.get("/")
def read(session: dr.Session = Depends(get_db)):
    db = dr.read_todo(session)
    return db


@app.post("/create/")
def create(todo: str, session: dr.Session = Depends(get_db)):
    todo_new = dr.Item(todo=todo)
    answer = dr.create_todo(session, todo_new)
    return answer


@app.put("/update/{id}/")
def update(id: int, todo: str, session: dr.Session = Depends(get_db)):
    answer = dr.update_todo(session, id, todo)
    return answer


@app.delete("/delete/{id}")
def update(id: int, session: dr.Session = Depends(get_db)):
    answer = dr.delete_todo(session, id)
    return answer
