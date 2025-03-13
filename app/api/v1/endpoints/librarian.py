from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Book, User
from app.schemas.book import BookCreate, BookUpdate, Book as BookSchema
from app.dependencies import get_current_librarian
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add-book", response_model=BookSchema)
def add_book(book: BookCreate, db: Session = Depends(get_db), librarian: User = Depends(get_current_librarian)):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.post("/categorize-book")
def categorize_book(book_id: int, category: str, db: Session = Depends(get_db), librarian: User = Depends(get_current_librarian)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db_book.category = category
        db.commit()
        db.refresh(db_book)
        return {"message": "Book categorized successfully"}
    return {"message": "Book not found"}
