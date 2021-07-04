from typing import List
import datetime as _dt
import pydantic as _pydantic


class _PostBase(_pydantic.BaseModel):
    text: str


class PostCreate(_PostBase):
    pass


class Post(_PostBase):
    id: int
    id_client: int
    date_created: _dt.date
    date_last_updated: _dt.date

    class Config:
        orm_mode = True


class PostPrediction(Post):
    sentiment: str
    percent_joy: float
    percent_fear: float
    percent_anger: float
    percent_sadness: float


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
