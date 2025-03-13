from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.schemas.book import BookCreate, BookUpdate, Book
from app.crud.book import create_book, get_book, get_books, update_book, delete_book
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Book)
async def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = create_book(db=db, book=book)
    return db_book

@router.get("/", response_model=List[Book])
async def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_books(db=db, skip=skip, limit=limit)

@router.get("/{book_id}", response_model=Book)
async def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = get_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put("/{book_id}", response_model=Book)
async def update_existing_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = update_book(db=db, book_id=book_id, book=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.delete("/{book_id}", response_model=Book)
async def delete_existing_book(book_id: int, db: Session = Depends(get_db)):
    db_book = delete_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book