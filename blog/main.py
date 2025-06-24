from fastapi import Depends, FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from blog.validity import check_valid_email, check_valid_name
from .schemas import Blog, ShowBlog, User
from typing import List
from .models import Base
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

from blog import models

app = FastAPI()

Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return {"message": "The id has been deleted from the database"}


@app.get("/blog", response_model=List[ShowBlog])
def fetch(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: Blog, db: Session = Depends(get_db)):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    blog = blog_query.first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found.",
        )

    blog_query.update({"title": request.title, "body": request.body})
    db.commit()
    return {"message": "Updated Successfully"}


@app.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=ShowBlog)
def fetch_single_blog(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )
    return blog


@app.post("/user", status_code=status.HTTP_201_CREATED)
def create_user(request: User, db: Session = Depends(get_db)):
    new_user = models.User(
        name=request.name, email=request.email, password=request.password
    )
    if not check_valid_email(request.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Please enter a valid email",
        )
    elif not check_valid_name(request.name):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Please enter a valid Name",
        )
    else:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
