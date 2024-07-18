from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from .. import models,schemas,utils,oauth2
from typing import Optional,List
from sqlalchemy.orm import Session
from ..database import get_db
from sqlalchemy import func
router=APIRouter(
prefix="/posts",tags=['posts'])

@router.get("/")#,response_model=List[schemas.PostOut])
async def get_posts(db: Session=Depends(get_db),current_user: int =Depends(oauth2.get_current_user),limit: int =5,skip: int=0,search: Optional[str]=" "):
        posts=db.query(models.Post,func.count(models.Vote.post_id)).join(models.Vote,models.Post.id==models.Vote.post_id).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
        results=db.query(models.Post,func.count("*").label("votes")).join(models.Vote,models.Vote.post_id==models.Post.id).group_by(models.Post.id)
        g=db.query(models.Post).join(models.Vote,models.Post.id==models.Vote.post_id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
        
        print(results)
        
        return g
        #posts=db.query(models.Post).filter(models.Post.owner_id==current_user.id).all()
       # return posts
       
        #cursor.execute("select * from fastapi")
       # posts=cursor.fetchall()
        #print(posts)
        return posts
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
async def create_post(post: schemas.PostCreate, db: Session=Depends(get_db),current_user: int =Depends(oauth2.get_current_user)):
       # print(current_user.id)
        new_post=models.Post(owner_id=current_user.id,**post.dict())
        #new_post=models.Post(title=post.title,content=post.content,published=post.published)
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return new_post
        
        #cursor.execute("insert into fastapi(title,content) values(%s,%s) returning *",(new_post.title,new_post.content))
        #post=cursor.fetchone()
        #print(post)
        #conn.commit()
      #  return {"wow":"post created succesfully"
@router.get("/{id}",response_model=schemas.Post)
async def get_post(id: int,response:Response,db: Session=Depends(get_db),current_user: int =Depends(oauth2.get_current_user)):
	#cursor.execute("select * from fastapi where id=%s",(str(id),))
	#post=cursor.fetchone()
	post=db.query(models.Post).filter(models.Post.id==id).first()
	if not post:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} is not found")
	print(post)
	return post
		#response.status_code=404
		#response.status_code=status.HTTP_404_NOT_FOUND
		#return {"message":f"post with id: {id} is not found"}
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int,db: Session=Depends(get_db),current_user: int =Depends(oauth2.get_current_user),limit: int=5):
	#cursor.execute("delete from fastapi where id=%s returning *",(str(id),))
	#deleted_post=cursor.fetchone()
	#conn.commit()
	post_query=db.query(models.Post).filter(models.Post.id==id)
	post=post_query.first()
	if post ==None:
		raise HTTPException(status_code=HTTP_404_NOT_FOUND,detail=f"post with id {id} is no where to be seen")
	if post.owner_id != current_user.id:
		raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Not Authorized to do requested action")
	post_query.delete(synchronize_session=False)
	db.commit()
	return {Response(status_code=status.HTTP_204_NO_CONTENT)}
@router.put("/{id}",response_model=schemas.Post)
async def  update_post(id: int,pot: schemas.PostCreate,db: Session=Depends(get_db),current_user: int =Depends(oauth2.get_current_user)):
	#cursor.execute("update fastapi set title=%s,content=%s where id=% returning *",(pot.title,pot.content,str(id)))
	#up_d=cursor.fetchone()
	#print(up_d)
	#conn.commit()
	post_query=db.query(models.Post).filter(models.Post.id==id)
	post=post_query.first()
	if post==None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id :{id} doesnot exist")
	#post_query.update({"title":"hey","content":"heelo"})
	if post.owner_id !=current_user.id:
		raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Not Authorized to perform requested action")
	post_query.update(pot.dict(),synchronize_session=False)
	db.commit()
	return post_query.first()