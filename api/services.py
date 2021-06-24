import sqlalchemy.orm as _orm
import datetime as _dt

import api.database as _database
import api.models as _models
import api.schemas as _schemas


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create some client functions
def create_client(db: _orm.Session, client: _schemas.ClientCreate):
    db_user = _models.Client(first_name=client.first_name, last_name=client.last_name, mail=client.mail,
                             phone=client.phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_clients(db: _orm.Session, skip: int, limit: int):
    return db.query(_models.Client).offset(skip).limit(limit).all()


def delete_client(db: _orm.Session, id: int):
    db.query(_models.Client).filter(_models.Client.id == id).delete()
    db.commit()


def get_client(db: _orm.Session, client_id: int):
    return db.query(_models.Client).filter(_models.Client.id == client_id).first()


def update_client(db: _orm.Session, id: int, client: _schemas._ClientBase):
    db_client = get_client(db=db, client_id=id)
    db_client.last_name = client.last_name
    db_client.first_name = client.first_name
    db_client.mail = client.mail
    db_client.phone = client.phone
    db.commit()
    db.refresh(db_client)
    return db_client


# Create some message functions
def get_posts(db: _orm.Session, skip: int = 0, limit: int = 10):
    return db.query(_models.Message).offset(skip).limit(limit).all()


def create_message(db: _orm.Session, id_client: int, message: _schemas.MessageCreate):
    db_message = _models.Message(text=message.text, id_client=id_client)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def get_post(db: _orm.Session, message_id: int):
    return db.query(_models.Message).filter(_models.Message.id == message_id).first()


def update_message(db: _orm.Session, id: int, message: _schemas.Message):
    db_message = get_post(db=db, message_id=id)
    db_message.text = message.text
    db_message.date_last_updated = _dt.datetime.utcnow
    db.commit()
    db.refresh(db_message)
    return db_message
