from pydantic import BaseModel
from datetime import datetime

class Book(BaseModel):
    id: int
    title: str
    author: str
    category: str

class User(BaseModel):
    id: int
    username: str
    role: str  # 'librarian' or 'customer'

class LendingRecord(BaseModel):
    id: int
    book_id: int
    customer_id: int
    lend_date: datetime
    return_date: datetime
    fine: float
