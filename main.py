from typing import List

from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

origins = ["*"]


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/cases/", response_model=schemas.Case)
def create_case(case: schemas.Case, db: Session = Depends(get_db)):
    return crud.create_case(db, case=case)


@app.get("/cases/", response_model=List[schemas.GetCase])
def read_cases(db: Session = Depends(get_db)):
    cases = crud.get_cases(db)
    return cases


@app.get("/cases/{case_id}", response_model=schemas.GetCase)
def read_case(case_id: int, db: Session = Depends(get_db)):
    db_case = crud.get_case(db, case_id=case_id)
    if db_case is None:
        raise HTTPException(status_code=404, detail="Case not found")

    return db_case


@app.put("/cases/{case_id}", response_model=schemas.Case)
def post_case(case_id: int, case: schemas.Case, db: Session = Depends(get_db)):
    db_case = crud.get_case(db, case_id=case_id)
    if db_case is None:
        raise HTTPException(status_code=404, detail="Case not found")

    crud.update_whole_case(db, case=case, case_id=case_id)
    return db_case


@app.patch("/cases/{case_id}", response_model=schemas.Case)
async def patch_case(case_id: int, case: Request, db: Session = Depends(get_db)):
    print(case)
    case = await case.json()
    db_case = crud.update_some_case(db, case=case, case_id=case_id)

    return db_case


@app.delete("/cases/{case_id}", response_model=schemas.Case)
def delete_case(case_id: int, db: Session = Depends(get_db)):
    db_case = crud.get_case(db, case_id=case_id)
    if db_case is None:
        raise HTTPException(status_code=404, detail="Case not found to delete")
    crud.delete_case(db, case_id=case_id)

    return db_case
