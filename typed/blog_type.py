from pydantic import BaseModel


class Blogbase(BaseModel):
    title: str
    content: str

    class config:
        orm_mode = True
