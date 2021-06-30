from typing import List

import fastapi as _fastapi
import sqlalchemy.orm as _orm

import api.schemas as _schemas
import api.services as _services

app = _fastapi.FastAPI()

_services.create_database()


# ----- CREATE COACH REQUESTS ----- #
@app.post("/clients/")
def create_client(client: _schemas.ClientCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return _services.create_client(db=db, client=client)


@app.delete("/clients/")
def delete_client(id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    client = _services.get_client(db=db, id=id)
    if client is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this client does not exist"
        )
    else:
        _services.delete_client(db=db, id=id)
        return f"User with id {id} has been successfully deleted"


@app.get("/clients/", response_model=List[_schemas.Client])
def read_clients(
        skip: int = 0,
        limit: int = 10,
        db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    clients = _services.get_clients(db=db, skip=skip, limit=limit)
    return clients


@app.get("/clients/{id}")
def read_client(
        id: int,
        db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    client = _services.get_client(db=db, id=id)
    return client


@app.put("/clients/{client_id}")
def update_client(
        client_id: int,
        client: _schemas._ClientBase,
        db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    is_in_list = _services.get_client(db=db, id=client_id)
    if is_in_list is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this client does not exist"
        )
    else:
        return _services.update_client(db=db, id=client_id, client=client)


# ----- CREATE POST REQUESTS ----- #
@app.post("/clients/{user_id}/post/")
def create_post(post: _schemas.PostCreate,
                user_id: int,
                db: _orm.Session = _fastapi.Depends(_services.get_db)
                ):
    return _services.create_post(db=db, post=post, user_id=user_id)


@app.put("/clients/{user_id}/post/")
def update_post(post: _schemas.PostCreate,
                user_id: int,
                db: _orm.Session = _fastapi.Depends(_services.get_db)):
    is_in_list = _services.get_posts(db=db, id_client=user_id)
    if is_in_list is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry, you are looking for post that does not exist"
        )
    else:
        return _services.update_post(db=db, user_id=user_id, post=post)


@app.get("/clients/{user_id}/post/", response_model=List[_schemas.Post])
def read_post(
        user_id: int,
        db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    posts = _services.get_posts(db=db, id_client=user_id)
    return posts
