<<<<<<< HEAD
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Setup Database Engine
engine = create_engine(os.getenv("DATABASE_URL"), poolclass=NullPool)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session
=======
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:vekariya2002@db.udftcdkerpezzoblentv.supabase.co:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

>>>>>>> a2600ba (update 30/12/2025- 4pm)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
<<<<<<< HEAD
        db.close()
=======
        db.close()
>>>>>>> a2600ba (update 30/12/2025- 4pm)
