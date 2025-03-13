from sqlalchemy import Column, Integer, DateTime, Float
from app.database import Base

class LendingRecord(Base):
    __tablename__ = "lending_records"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, index=True)
    customer_id = Column(Integer, index=True)
    lend_date = Column(DateTime, index=True)
    return_date = Column(DateTime, index=True)
    fine = Column(Float, index=True)
