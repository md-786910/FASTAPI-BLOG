from fastapi.routing import APIRouter, HTTPException
from typed import user_type
from models import user_model
from database import db_dependencies, engine
from utils import password
from models import user_model


# repos
from repos import user_repos

# create database table
user_model.Base.metadata.create_all(bind=engine)


userRouter = APIRouter(tags=["users"], prefix="/api/v1")


# Login
@userRouter.post("/login")
async def user_login(user: user_type.userLogin, db: db_dependencies):
    if user is not None:
        user = user_repos.login_user(user, db)
        return user
    else:
        raise HTTPException(status=404, detail="Invalid email or password")


# Register
@userRouter.post(
    "/register",
)
async def user_register(user: user_type.userRegister, db: db_dependencies):
    if user is not None:
        users = user_repos.register_user(user, db)
        return users
    else:
        raise HTTPException(status=404, detail="field is missing")


# delete user
@userRouter.delete("/delete{userId}")
async def user_delete(
    userId: int,
    db: db_dependencies,
):
    user = db.query(user_model.Users).filter(user_model.Users.id == userId).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return responseJson()
    return {"status": 200, "message": "deleted successfully"}


# all user
@userRouter.get("/userAll", response_model=list[user_type.allUser])
async def user_all(db: db_dependencies):
    users = db.query(user_model.Users).all()
    return users
