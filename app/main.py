# filepath: c:\Users\rohin\OneDrive\Desktop\Library\app\main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.api.v1.endpoints import books, librarian, customer
from app.database import engine
from app.models import Book, User, LendingRecord
import os

app = FastAPI()

app.include_router(books.router, prefix="/api/v1/books", tags=["books"])
app.include_router(librarian.router, prefix="/api/v1/librarian", tags=["librarian"])
app.include_router(customer.router, prefix="/api/v1/customer", tags=["customer"])

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open(os.path.join("app", "templates", "index.html")) as f:
        return HTMLResponse(content=f.read(), status_code=200)

# Create the database tables
Book.metadata.create_all(bind=engine)
User.metadata.create_all(bind=engine)
LendingRecord.metadata.create_all(bind=engine)