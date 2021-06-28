from typing import List

import fastapi as _fastapi
import sqlalchemy.orm as _orm

import api.schemas as _schemas
import api.services as _services

app = _fastapi.FastAPI()

_services.create_database()


# Create coach requests
@app.post("/clients/")
def create_client(client: _schemas.ClientCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return _services.create_client(db=db, client=client)


@app.delete("/clients/")
def delete_client(id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    client = _services.get_client(db=db, client_id=id)
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


# Create post requests
@app.post("/clients/{client_id}/post")
def create_post(post: _schemas.PostCreate,
                id_client: int,
                db: _orm.Session = _fastapi.Depends(_services.get_db)
                ):
    return _services.create_post(db=db, id_client=id_client, post=post)


@app.put("/post/{post_id}")
def update_post(post: _schemas._PostBase,
                id_client: int,
                id_post: int,
                db: _orm.Session = _fastapi.Depends(_services.get_db)):
    is_in_list = _services.get_post(db=db, id_post=id_post)
    if is_in_list is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry, you are looking for post that does not exist"
        )
    else:
        return _services.update_post(db=db, id_post=id_post, post=post)


@app.get("/clients/{client_id}/post")
def read_post(
        skip: int = 0,
        limit: int = 10,
        db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    posts = _services.get_posts(db=db, skip=skip, limit=limit)
    return posts
