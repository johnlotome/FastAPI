from typing import Optional, List
from fastapi import FastAPI, HTTPException, status, Response, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2 
from psycopg2.extras import RealDictCursor #To give the column names
import time
from . import models, schema, utils
from .database import engine, get_db
from sqlalchemy.orm import Session



models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True: 
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
                                password='root', cursor_factory=RealDictCursor)
        
        cursor =  conn.cursor()
        print("Database connection was succesfull!!")
        break
    except Exception as error:
        print("Connection Failed with error: ", error)
        time.sleep(2)

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {
    "title": "favorite foods", "content": "I like pizza", "id": 2
}]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i 

#Path operator 
@app.get("/")    #Decorator - turns the function below to a path operator. The /indicates the root path
async def root():
    return {"message": "Hello World"}


