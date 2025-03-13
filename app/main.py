from fastapi import FastAPI
from app.api.v1.endpoints import books, librarian, customer
from app.database import engine
from app.models import Book, User, LendingRecord

app = FastAPI()

app.include_router(books.router, prefix="/api/v1/books", tags=["books"])
app.include_router(librarian.router, prefix="/api/v1/librarian", tags=["librarian"])
app.include_router(customer.router, prefix="/api/v1/customer", tags=["customer"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Library Management System"}

# Create the database tables
Book.metadata.create_all(bind=engine)
User.metadata.create_all(bind=engine)
LendingRecord.metadata.create_all(bind=engine)