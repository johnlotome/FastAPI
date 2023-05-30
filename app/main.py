from fastapi import FastAPI
import models
from database import engine
from routers import post, user, auth, vote
from config import settings


print(settings.DATABASE_URL)

# models.Base.metadata.create_all(bind=engine)    ----using alembic instead

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

#Path operator 
@app.get("/")    #Decorator - turns the function below to a path operator. The /indicates the root path
async def root():
    return {"message": "Hello World"}


