fromfrom fastapi import FastAPI,Response,status,HTTPException
from pydantic import BaseModel
from fastapi.params iimportmport Body
from typing import Optional
from random import randrange
import mysql.connector
import time
from sql alchemy.orm import Session
from . import models
from .database import engine,SessionLocal
models.Base.metadata.create_all(bind=engine)
app=FastAPI()
def get_db():
	db=SessionLocal()
	try:
		yield db
	finally:
			db.close()
			
class Post(BaseModel):
        title: str
        content: str
        published: bool =True
        rating: Optional[int] = None
my_posts=[{"title":"title of post1","content":"content of post1","id":1},{"title":"hello","content":"much love","id":2}]
while True:
	try:
		conn=mysql.connector.connect(
		host="localhost",
		user="root",
		password="MyN3wP4ssw0rd",
		database="izo")
		cursor=conn.cursor()
		print("database connection was succesfull")
		break
	except Exception as error:
		print("connection to the database failed")
		print("error",error)
		time.sleep(2)


def find_post(id):
	for p in my_posts:
		if p["id"] ==id:
			return p
def find_index(id):
		for i,p in enumerate(my_posts):
			if p["id"]==id:
				return i
		
@app.get("/sqlalchemy")
async def test_posts(db: Session= Depends(get_db)):
	return {"status":"success"}	
@app.get("/login")
async def root():
        return {"hello thanks for logging in"}
@app.get("/posts")
async def get_posts():
        cursor.execute("select * from fastapi")
        posts=cursor.fetchall()
        print(posts)
        return {"data":posts}
@app.post("/post")
async def create_post(new_post: Post):
        cursor.execute("insert into fastapi(title,content) values(%s,%s) returning *",(new_post.title,new_post.content))
        post=cursor.fetchone()
        print(post)
        conn.commit()
        return {"wow":"post created succesfully"}
@app.get("/posts/latest")
async def latest_post():
	post=my_posts[len(my_posts)-1]
	return {"detali":post}
@app.get("/posts/{id}")
async def get_post(id: int,response: Response):
	cursor.execute("select * from fastapi where id=%s",(str(id),))
	post=cursor.fetchone()
	if not post:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} is not found")
		#response.status_code=404
		#response.status_code=status.HTTP_404_NOT_FOUND
		#return {"message":f"post with id: {id} is not found"}
	print(post)
	return {"post detail":post}
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
	cursor.execute("delete from fastapi where id=%s returning *",(str(id),))
	deleted_post=cursor.fetchone()
	conn.commit()
	if deleted_post ==None:
		raise HTTPException(status_code=HTTP_404_NOT_FOUND,detail=f"post with id {id} was not found")
	return {Response(status_code=status.HTTP_204_NO_CONTENT)}
@app.put("/posts/{id}")
async def  update_post(id: int,pot: Post):
	cursor.execute("update fastapi set title=%s,content=%s where id=% returning *",(pot.title,pot.content,str(id)))
	up_d=cursor.fetchone()
	print(up_d)
	conn.commit()
	if up_d==None:
		raise HTTPException(status_code=202,detail=f"post updated  successfully")
	return {"new post":"updated successfully"}
	
	