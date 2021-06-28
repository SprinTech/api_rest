import sqlalchemy.orm as _orm
import datetime as _dt

import api.database as _database
import api.models as _models
import api.schemas as _schemas


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    """Create connection to database"""
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create some client functions
def create_client(db: _orm.Session, client: _schemas.ClientCreate):
    """Add new client to database

    Parameters:
        -> db: connection to SQL database
        -> client: get scheme of client create function

    Returns:
        -> dic: User first name, last name, mail and phone

    """
    db_user = _models.Client(first_name=client.first_name, last_name=client.last_name, mail=client.mail,
                             phone=client.phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_clients(db: _orm.Session, skip: int, limit: int):
    """Get list of all clients stored in database

    Parameters:
        -> db: connection to SQL database
        -> skip (int): number of element to skip from 0
        -> limit (int): maximum number of element to return

    Returns:
        -> List of dic: Information about all client stored in database

    """
    return db.query(_models.Client).offset(skip).limit(limit).all()


def delete_client(db: _orm.Session, id: int):
    """Delete client from database

    Parameters:
        -> db: connection to SQL database
        -> id (int): client id

    """
    db.query(_models.Client).filter(_models.Client.id == id).delete()
    db.commit()


def get_client(db: _orm.Session, id: int):
    """Get information about a client

    Parameters:
        -> db: connection to SQL database
        -> id (int): id of client

    Returns:
        -> Query: information about a client

    """
    return db.query(_models.Client).filter(_models.Client.id == id).first()


def update_client(db: _orm.Session, id: int, client: _schemas._ClientBase):
    """Update information about a client stored in the database

    Parameters:
        -> db: connection to SQL database
        -> id (int): id of client
        -> client (class): information about a client

    Returns:
        -> List: information updated about a client

    """
    db_client = get_client(db=db, id=id)
    db_client.last_name = client.last_name
    db_client.first_name = client.first_name
    db_client.mail = client.mail
    db_client.phone = client.phone
    db.commit()
    db.refresh(db_client)
    return db_client


# Create some post functions
def get_posts(db: _orm.Session, skip: int = 0, limit: int = 10):
    """Get all posts stored in database

    Parameters:
        -> db: connection to SQL database
        -> skip (int): number of element to skip from 0
        -> limit (int): maximum number of element to return

    Returns:
        -> Query: Information about all posts stored in database

    """
    return db.query(_models.post).offset(skip).limit(limit).all()


def create_post(db: _orm.Session, id_client: int, post: _schemas.PostCreate):
    """Add new post to database

    Parameters:
        -> db: connection to SQL database
        -> id_client (int): if of client
        -> post (class): information about a post

    Returns:
        -> Dic:
    """
    db_post = _models.post(text=post.text, id_client=id_client)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(db: _orm.Session, id_post: int):
    """Get all post written by a single client

    Parameters:
        -> db: connection to SQL database
        -> id_post (int): id of post

    Returns:
        ->
    """
    return db.query(_models.post).filter(_models.post.id == id_post).first()


def update_post(db: _orm.Session, id_post: int, post: _schemas.Post):
    db_post = get_post(db=db, id_post=id_post)
    db_post.text = post.text
    db_post.date_last_updated = _dt.datetime.utcnow()
    db.commit()
    db.refresh(db_post)
    return db_post
