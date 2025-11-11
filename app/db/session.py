import os 
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE =  os.getenv("DATABASE_URL", "sqlite:///./dev.db")

engine = create_engine(DATABASE, echo=False, future=True, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

Base = declarative_base()

def get_session() -> Generator:
    """
    Provide a transactional scope around a series of operations.
    Use as:
        with get_session() as session:
            ...
    Or as a FastAPI dependency:
        def endpoint(session = Depends(get_session)):
            ...
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()