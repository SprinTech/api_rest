import datetime as _dt
import sqlalchemy as _sql
import sqlalchemy.orm as _orm

import api.database as _database


class Client(_database.Base):
    __tablename__ = "Client"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    first_name = _sql.Column(_sql.String)
    last_name = _sql.Column(_sql.String)
    mail = _sql.Column(_sql.String, unique=True)
    phone = _sql.Column(_sql.String(length=10), unique=True, default="empty")


class Message(_database.Base):
    __tablename__ = "Message"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    id_client = _sql.Column(_sql.Integer, _sql.ForeignKey("Client.id"))
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    text = _sql.Column(_sql.Text)
    sentiment = _sql.Column(_sql.String)
    positive = _sql.Column(_sql.Float())
    neutral = _sql.Column(_sql.Float())
    negative = _sql.Column(_sql.Float())
