from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine) #Cria as tabelas no PostgreSQL caso não exista
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/students/', response_model=schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db())): #Define função create_student e recebe 2 parametros.
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get('/students/', response_model=List[schemas.StudentResponse])
def read_students(db: Session = Depends(get_db())):
    students = db.query(models.Student).all()
    return students