from fastapi import Depends, HTTPException
from app.models.user import User

def get_current_user():
    # Logic to get current user
    return User(id=1, username="testuser", role="customer")

def get_current_librarian(current_user: User = Depends(get_current_user)):
    if current_user.role != "librarian":
        raise HTTPException(status_code=403, detail="Not authorized")
    return current_user

def get_current_customer(current_user: User = Depends(get_current_user)):
    if current_user.role != "customer":
        raise HTTPException(status_code=403, detail="Not authorized")
    return current_user
