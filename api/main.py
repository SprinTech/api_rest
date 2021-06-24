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
    _services.create_client(db=db, client=client)
    return f"Client {client.last_name} {client.first_name} has been successfully added"


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
    is_in_list = _services.get_client(db=db, client_id=client_id)
    if is_in_list is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this client does not exist"
        )
    else:
        _services.update_client(db=db, id=client_id, client=client)
        return f"Information about user with id {id} have been updated"


# Create message requests
@app.post("/clients/{client_id}/post")
def create_message(message: _schemas.MessageCreate, id_client: int,
                   db: _orm.Session = _fastapi.Depends(_services.get_db)):
    _services.create_message(db=db, id_client=id_client, message=message)
    return f"Message has been successfully registered"


@app.put("/post/{post_id}")
def update_message(
        post_id: int,
        post: _schemas.Message,
        db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    is_in_list = _services.get_messages(db=db, message_id=post_id)
    if is_in_list is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry message you are looking for does not exist"
        )
    else:
        _services.update_message(db=db, id=post_id, message=post)
        return f"Message has been successfully updated"
