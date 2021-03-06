import datetime as _dt
import sqlalchemy as _sql

import api.database as _database


class Client(_database.Base):
    __tablename__ = "Client"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    first_name = _sql.Column(_sql.String)
    last_name = _sql.Column(_sql.String)
    mail = _sql.Column(_sql.String, unique=True, default="empty")
    phone = _sql.Column(_sql.String(length=10), unique=True, default="empty")


class Post(_database.Base):
    __tablename__ = "Post"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    id_client = _sql.Column(_sql.Integer, _sql.ForeignKey("Client.id"))
    date_created = _sql.Column(_sql.Date, default=_dt.datetime.utcnow)
    date_last_updated = _sql.Column(_sql.Date, default=_dt.datetime.utcnow)
    text = _sql.Column(_sql.Text)
    sentiment = _sql.Column(_sql.String, default="empty")
    percent_joy = _sql.Column(_sql.Float(), default="0")
    percent_fear = _sql.Column(_sql.Float(), default="0")
    percent_sadness = _sql.Column(_sql.Float(), default="0")
    percent_anger = _sql.Column(_sql.Float(), default="0")
