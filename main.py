from typing import Union
from fastapi import FastAPI
from database import engine, Base, Forum
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)
import shemas

app = FastAPI()

@app.get("/")
def read_root():
    return "Moj app"

@app.post("/add")
def add_text(forum: shemas.Forum):
    """
        API call for adding text
    """
    session = Session(bind=engine, expire_on_commit= False)
    forumDB = ToDo(text = forum.task)
    session.add(forumDB)
    session.commit()
    id = forumDB.id
    session.close()
    return f"Created new text with id {id}"

@app.delete("/delete/{id}")
def delete_text(id: int):
    session = Session(bind=engine, expire_on_commit=False)
    forumDB = session.query(Forum).filter(Forum.id == id).first()
    if not forumDB:
        return f"No text found with ID {id}", 404
    session.delete(forumDB)
    session.commit()
    session.close()
    return f"Deleted zapis with ID {id}"

@app.put("/update/{id}")
def update_text():
    return "Update"

@app.get("/get/{id}")
def get_text():
    return "get"

@app.get("/list")
def get_all_texts():
    session = Session(bind=engine, expire_on_commit=False)
    text_list = session.query(Forum).all()
    session.close()
    return forum_list