from fastapi import FastAPI

from fastapi import APIRouter, Depends
from models import Candidate
from database import get_db

from sqlalchemy.orm import Session

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "HR Analytics Dashboard"
    }

@app.get("/details")
def details( db: Session = Depends(get_db)):
    candidates = db.query(Candidate).all()
    data = []
    for candiate in candidates:
        data.append(candiate.name)

    return{

        "name":candiate.name
    }   
