from typing import List
import datetime as _dt
import pydantic as _pydantic


class _PostBase(_pydantic.BaseModel):
    text: str


class Post(_PostBase):
    id: int
    id_client: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime
    text: str

    class Config:
        orm_mode = True


class PostCreate(_PostBase):
    pass


class PostPrediction(Post):
    emotion: str
    positive: float
    neutral: float
    negative: float


class _ClientBase(_pydantic.BaseModel):
    first_name: str
    last_name: str
    mail: str
    phone: str


class ClientCreate(_ClientBase):
    pass


class Client(_ClientBase):
    id: int

    # post: List[post] = []

    class Config:
        orm_mode = True
