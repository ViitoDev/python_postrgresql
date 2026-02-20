from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import sessionmaker
from dotenv import load_dotenv

DATABASE_URL = "postgresql://username:password@localhost/school"

engine = create_engine(DATABASE_URL) #Comunicate with FastAPI
SessionLocal = sessionmaker(bind=engine) #Conn
Base = declarative_base() #Create the entities