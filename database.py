from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends
from typing import Annotated

# SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

SQLALCHEMY_DATABASE_URL = "postgres://tuteck_storag_user:Ary0gn7Z5sahssDDWnVjFXQ9V4sZlIgW@dpg-ckbrsnmct0pc7382b28g-a.oregon-postgres.render.com/tuteck_storag"

# connect_args={"check_same_thread": False}

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     future=True,
# )

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,  # To prevent stale connections
    # connect_args={"sslmode": "require"},  # Add SSL mode if required
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# create dependency
db_dependencies = Annotated[Session, Depends(get_db)]
