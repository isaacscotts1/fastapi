
from fastapi import FastAPI,Response,status,HTTPException,Depends
from pydantic import BaseModel
from fastapi.params import Body
from typing import Optional,List
from random import randrange
import mysql.connector
import time
from fastapi.middleware.cors import CORSMiddleware
#from passlib.context import CryptContext
from sqlalchemy.orm import Session
from . import models,schemas,utils
from .database import engine,SessionLocal,get_db
from .routers import post,user,auth,vote

#pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
#models.Base.metadata.create_all(bind=engine)
app=FastAPI()
origins=["*"]
app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=["*"],allow_headers=["*"],)
			
			

#my_posts=[{"title":"title of post1","content":"content of post1","id":1},{"title":"hello","content":"much love","id":2}



				
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
@app.get("/isaac scotts")		
async def test_posts(db: Session=Depends(get_db)):
	posts=db.query(models.Post).all()
	return {"message":"you've done it"}	
@app.get("/")
async def root():
        return {"hello thanks for logging in"}


