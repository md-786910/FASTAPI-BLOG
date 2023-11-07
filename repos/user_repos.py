from fastapi import HTTPException, status
from utils import password
from models import user_model
from fastapi.responses import JSONResponse

from jwt_user import jwtSign


def register_user(user, db):
    hash_password = password.hashPassword(user.password)
    userExist = (
        db.query(user_model.Users).filter(user_model.Users.email == user.email).first()
    )
    if userExist:
        return JSONResponse(status_code=404, content={"message": "user already exists"})
    else:
        user_db = user_model.Users(
            name=user.name, email=user.email, password=hash_password
        )
        if user_db:
            db.add(user_db)
            db.commit()
            db.refresh(user_db)
            return {"status": "201", "message": "missing", "user": user_db}


# end
def login_user(user, db):
    try:
        email = user.email
        users = (
            db.query(user_model.Users).filter(user_model.Users.email == email).first()
        )
        # # verify password
        if password.verifyPassword(user.password, users.password):
            # create token
            token = jwtSign.create_access_token(
                data={"sub": users.email, "id": users.id, "name": users.name}
            )
            return {
                "message": "login success",
                "token": token,
                "token_type": "Bearer",
                "data": users,
            }
        else:
            return JSONResponse(
                status_code=404, content={"message": "user already exists"}
            )
            # return {"message": "password does not matched", "status": 404}
    except Exception as e:
        return f"Error is :{e}"


# delete user
