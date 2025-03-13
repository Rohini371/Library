from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.models import Book, User, LendingRecord
from app.schemas.book import Book as BookSchema
from app.dependencies import get_current_customer
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/lend-book", response_model=BookSchema)
def lend_book(book_id: int, db: Session = Depends(get_db), customer: User = Depends(get_current_customer)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        lending_record = LendingRecord(book_id=book_id, customer_id=customer.id, lend_date=datetime.now())
        db.add(lending_record)
        db.commit()
        db.refresh(lending_record)
        return db_book
    return {"message": "Book not found"}

@router.get("/lending-records")
def get_lending_records(db: Session = Depends(get_db), customer: User = Depends(get_current_customer)):
    records = db.query(LendingRecord).filter(LendingRecord.customer_id == customer.id).all()
    return {"lending_records": records}
