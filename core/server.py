from pydantic import BaseModel
import data_related as dr
from fastapi import FastAPI, Depends
from typing import List 


def get_db():
    db = dr.SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()
dr.Base.metadata.create_all(bind=dr.engine,checkfirst=True)


@app.get("/")
def read(session: dr.Session = Depends(get_db)):
    db = dr.read_todo(dr.SessionLocal())
    return db

@app.post("/new_todo")
def post(do:str, session: dr.Session = Depends(get_db)):
    pass
    # create_todo(db: Session, todo: Item)
    


# @app.patch()
