from fastapi.routing import APIRouter
from fastapi import Depends
from database import db_dependencies
from jwt_user import outh2
from typed import blog_type
from models.user_model import Blog, Users

blogRouter = APIRouter(tags=["blogs"], prefix="/api/v1/blog")


@blogRouter.post("/create")
async def blog_create(
    blog: blog_type.Blogbase,
    db: db_dependencies,
    current_user=Depends(outh2.get_current_user),
):
    blogs = Blog(**blog.dict(), user_id=current_user["id"])
    if blogs:
        db.add(blogs)
        db.commit()
        db.refresh(blogs)
        return blogs
    else:
        return {"status": 404, "message": "Couldn't find id'"}


@blogRouter.get("/getAll")
async def get_blog_all(db: db_dependencies):
    return db.query(Blog).all()


@blogRouter.get("/{id}")
async def get_blog_By_id(id: int):
    return f"Blog of id : {id}"
