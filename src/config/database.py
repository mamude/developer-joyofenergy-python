from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database settings
engine = create_engine("sqlite:///database.db", connect_args={"check_same_thread": False})
session_local = sessionmaker(autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


def get_db():
    """
    Create a database session

    Yields:
        Session: the database session
    """
    db = session_local()
    try:
        yield db
    finally:
        db.close()
