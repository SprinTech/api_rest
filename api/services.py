import sqlalchemy.orm as _orm
import datetime as _dt

import api.database as _database
import api.models as _models
import api.schemas as _schemas


def create_database():
    """Create database files in api folder"""
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
        -> db: establish conversation with database
        -> client: get scheme of client create function

    Returns:
        -> dictionary that contain client information : first name, last name, mail and phone

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
        -> db: establish conversation with database
        -> skip (int): number of element to skip from 0
        -> limit (int): maximum number of element to return

    Returns:
        -> list of dictionary that display information about all clients stored in database

    """
    return db.query(_models.Client).offset(skip).limit(limit).all()


def delete_client(db: _orm.Session, id: int):
    """Delete existing client from database

    Parameters:
        -> db: establish conversation with database
        -> id (int): client id

    """
    db.query(_models.Client).filter(_models.Client.id == id).delete()
    db.commit()


def get_client(db: _orm.Session, id: int):
    """Get information about a client

    Parameters:
        -> db: establish conversation with database
        -> id (int): id of client

    Returns:
        -> Information about client that match with id

    """
    return db.query(_models.Client).filter(_models.Client.id == id).first()


def update_client(db: _orm.Session, id: int, client: _schemas._ClientBase):
    """Update information about a client stored in the database

    Parameters:
        -> db: establish conversation with database
        -> id (int): id of client
        -> client (class): information about a client

    Returns:
        -> Information updated about a specified client

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
def get_post(db: _orm.Session, user_id: int):
    """Get all posts written by clients.

    Parameters:
        -> db: establish conversation with database
        -> skip (int): number of element to skip from 0
        -> limit (int): maximum number of element to return

    Returns:
        -> Last post created by client

    """
    return db.query(_models.Post).filter(_models.Post.id_client == user_id).order_by(
        _models.Post.date_last_updated.desc()).first()


def get_all_posts(db: _orm.Session, skip: int, limit: int):
    """Get list of all clients stored in database

    Parameters:
        -> db: establish conversation with database
        -> skip (int): number of element to skip from 0
        -> limit (int): maximum number of element to return

    Returns:
        -> list of dictionary that display information about all clients stored in database

    """
    return db.query(_models.Post).offset(skip).limit(limit).all()


def create_post(db: _orm.Session, post: _schemas.PostCreate, user_id: int, sentiment: str, percent_anger: float,
                percent_fear: float, percent_joy: float, percent_sadness: float):
    """Add new post to database

    Parameters:

        -> db: establish conversation with database
        -> id_client (int): if of client
        -> post (class): information about a post

    Returns:
        -> Class instance of post

    """
    db_post = _models.Post(text=post.text, id_client=user_id, sentiment=sentiment, percent_anger=percent_anger,
                           percent_fear=percent_fear, percent_joy=percent_joy, percent_sadness=percent_sadness)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_posts(db: _orm.Session, id_client: int):
    """Get all post written by a single client

    Parameters:
        -> db: establish conversation with database
        -> id_post (int): id of post

    Returns:
        -> All post filtered that match with specified id client

    """
    return db.query(_models.Post).filter(_models.Post.id_client == id_client).all()


def update_post(db: _orm.Session, post: _schemas.PostCreate, user_id: int, sentiment: str, percent_anger: float,
                percent_fear: float, percent_joy: float, percent_sadness: float):
    """Update post

    Parameters:
        -> db: establish conversation with database
        -> user_id (int): id of user
        -> post (class): information about a posts

    Returns:
        -> Class instance of post

    """
    db_post = get_post(db=db, user_id=user_id)
    db_post.text = post.text
    db_post.sentiment = sentiment
    db_post.percent_joy = percent_joy
    db_post.percent_fear = percent_fear
    db_post.percent_anger = percent_anger
    db_post.percent_sadness = percent_sadness
    db_post.date_last_updated = _dt.datetime.utcnow()
    db.commit()
    db.refresh(db_post)
    return db_post
