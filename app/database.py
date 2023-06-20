from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2 
from psycopg2.extras import RealDictCursor #To give the column names
import time
from config import settings

# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_URL}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}'
print(SQLALCHEMY_DATABASE_URL)



engine =  create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db =  SessionLocal()
    try:
        yield db
    finally:
        db.close()



# while True: 
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
#                                 password='root', cursor_factory=RealDictCursor)
        
#         cursor =  conn.cursor()
#         print("Database connection was succesfull!!")
#         break
#     except Exception as error:
#         print("Connection Failed with error: ", error)
#         time.sleep(2)