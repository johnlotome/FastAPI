from fastapi import FastAPI, HTTPException, status, Response, Depends, APIRouter
from app import oauth2
from typing import Optional, List
from sqlalchemy.orm import Session
from app import models, schema, utils
from app.database import engine, get_db
from sqlalchemy import func

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get("/", response_model=List[schema.PostOut])
def get_post(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
             limit: int = 10, skip: int = 0, search: Optional[str]=""):

    # print(current_user.id)
    # posts = db.query(models.Post).filter(
        # models.Post.owner_id == current_user.id, models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote,
                                    models.Post.id==models.Vote.post_id, 
                                    isouter=True).group_by(models.Post.id).order_by(func.count(models.Vote.post_id).desc()).\
                                        filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
      
    # print(results)
    # cursor.execute("""SELECT * FROM posts""") 
    # posts = cursor.fetchall()

    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.Post)
def create_posts(post: schema.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)): 
    # post_dict = post.dict()
    # post_dict['id'] = randrange(0, 10000000)
    # my_posts.append(post_dict)
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", (post.title,
    #                                                                                          post.content, post.published))
    # new_post =  cursor.fetchone()
    # conn.commit()
    ###print(**post.dict()) # (**) Unpacking dictionary
    # print(current_user.id)
    new_post = models.Post(owner_id = current_user.id,
        **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post) #RETURNING sql 
    return new_post


@router.get("/{id}", response_model=schema.PostOut)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    # post = cursor.fetchone()
    # post = db.query(models.Post).filter(models.Post.id == str(id)).first()

    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote,
                                    models.Post.id==models.Vote.post_id, 
                                    isouter=True).group_by(models.Post.id)\
                                    .filter(models.Post.id == str(id)).first()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    
    # if post.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #                         detail=f"Not authorized to perform requested action")
    
    return post



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'post with id: {id} does not exist')
    

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")
    
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}", response_model=schema.Post)
def update_post(id: int, updated_post: schema.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)): 
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published= %s WHERE id = %s RETURNING *""", (post.title, 
    #                     post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'post with id: {id} does not exist')
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")
    post_query.update(updated_post.dict(),
                      synchronize_session=False)
    db.commit()
    return post_query.first()