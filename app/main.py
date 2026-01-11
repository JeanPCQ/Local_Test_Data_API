from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, DateTime, JSON, create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
import time
import os

# ----------------------
# Database connection with retry
# ----------------------
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/testdata")

Base = declarative_base()
max_retries = 10
for attempt in range(max_retries):
    try:
        engine = create_engine(DATABASE_URL)
        conn = engine.connect()
        conn.close()
        print("Database connected!")
        break
    except OperationalError:
        print(f"Database not ready, retrying ({attempt+1}/{max_retries})...")
        time.sleep(2)
else:
    raise Exception("Could not connect to the database after multiple retries")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ----------------------
# FastAPI app
# ----------------------
app = FastAPI(title="Local Test Data API")

# Database model
class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    payload = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------------
# API endpoints
# ----------------------
@app.post("/records")
def create_record(record: dict, db: Session = Depends(get_db)):
    new_record = Record(
        type=record.get("type", "generic"),
        payload=record
    )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return {"id": new_record.id}

@app.get("/records")
def get_records(db: Session = Depends(get_db)):
    records = db.query(Record).all()
    return records
