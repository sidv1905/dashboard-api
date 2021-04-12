from sqlalchemy.orm import Session
import models, schemas


def get_cases(db: Session):
    return db.query(models.Case).all()


def get_case(db: Session, case_id: int):
    return db.query(models.Case).filter(models.Case.id == case_id).first()


def create_case(db: Session, case: schemas.Case):
    db_case = models.Case(**case.dict())

    db.add(db_case)
    db.commit()
    db.refresh(db_case)
    return db_case


def update_whole_case(db: Session, case: schemas.Case, case_id: int):
    db_case = db.query(models.Case).filter(models.Case.id == case_id)
    response = db_case.first()
    print(case.dict(), "inside put")
    db_case.update(case.dict(), synchronize_session=False)
    db.commit()

    return response


def delete_case(db: Session, case_id: int):
    db_case = db.query(models.Case).filter(models.Case.id == case_id)
    response = db_case.first()

    db_case.delete()
    db.commit()
    return response


def update_some_case(db: Session, case, case_id: int):
    db_case = db.query(models.Case).filter(models.Case.id == case_id).first()
    ''' "Branch": "dsasaddasd",
    "Method": "string",
    "Date": "2021-04-10",
    "Time": "string",
    "Category": "string",
    "SubCategory": "string",
    "Priority": "string",
    "Nature": "string",
    "Manager": "string",
    "Reporter": "string",
    "Status": "string"'''
    print(case, type(case), "patch me", db_case.Branch)
    if "Branch" in case:
        db_case.Branch = case["Branch"]
    if "Time" in case:
        db_case.Time = case["Time"]
    if "Category" in case:
        db_case.Category = case["Category"]
    if "SubCategory" in case:
        db_case.SubCategory = case["SubCategory"]
    if "Priority" in case:
        db_case.Priority = case["Priority"]
    if "Nature" in case:
        db_case.Nature = case["Nature"]
    if "Manager" in case:
        db_case.Manager = case["Manager"]
    if "Reporter" in case:
        db_case.Reporter = case["Reporter"]
    if "Status" in case:
        db_case.Status = case["Status"]
    if "Method" in case:
        db_case.Method = case["Method"]

    db.commit()
    return db_case

