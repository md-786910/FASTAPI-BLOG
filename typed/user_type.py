from pydantic import BaseModel


class userEmail(BaseModel):
    email: str


class userName(BaseModel):
    name: str


class userRegister(userEmail, userName):
    password: str


class userResponse(userRegister):
    id: int

    class config:
        orm_mode = True


class allUser(userEmail, userName):
    id: int

    class config:
        orm_mode = True


class userLogin(userEmail):
    password: str
