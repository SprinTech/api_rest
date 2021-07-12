from fastapi.testclient import TestClient
from api.database import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.main import app
from api.services import get_db
import pytest
import datetime as dt
import os

# create test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    """Activate testing session"""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


# ----- TEST CLIENT REQUESTS ----- #
def test_create_client():
    """Check if user is correctly added to database"""
    response = client.post(
        "/clients/",
        json={"first_name": "Dupont", "last_name": "Gérard", "mail": "g.dupont@gmail.com", "phone": "0655555555"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["mail"] == "g.dupont@gmail.com"
    assert data["phone"] == "0655555555"
    assert "id" in data
    user_id = data['id']

    response = client.get(f"/clients/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["mail"] == "g.dupont@gmail.com"
    assert data["phone"] == "0655555555"
    assert data["first_name"] == "Dupont"
    assert data["last_name"] == "Gérard"
    assert data["id"] == user_id


def test_update_client():
    """Check if information about existing user are correctly updated in database"""
    user_id = 1

    response = client.get(f"/clients/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["mail"] == "g.dupont@gmail.com"
    assert data["phone"] == "0655555555"
    assert data["id"] == user_id

    response = client.put(
        f"/clients/{user_id}",
        json={"first_name": "Durand", "last_name": "Benoît", "mail": "b.durand@gmail.com", "phone": "0654843516"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data['first_name'] == 'Durand'
    assert data['last_name'] == 'Benoît'
    assert data['mail'] == 'b.durand@gmail.com'
    assert data['phone'] == '0654843516'

    response = client.get(f"/clients/{user_id}")
    assert response.status_code == 200

    assert data['first_name'] == 'Durand'
    assert data['last_name'] == 'Benoît'
    assert data['mail'] == 'b.durand@gmail.com'
    assert data['phone'] == '0654843516'
    assert data['id'] == 1


def test_delete_client():
    """Check if client is correctly removed from database"""
    user_id = 1

    response = client.get(f"/clients/{user_id}")
    assert response.status_code == 200
    data = response.json()

    assert data['first_name'] == 'Durand'
    assert data['last_name'] == 'Benoît'
    assert data['mail'] == 'b.durand@gmail.com'
    assert data['phone'] == '0654843516'
    assert data['id'] == 1

    response = client.delete("/clients/")

    data = response.json()
    with pytest.raises(KeyError):
        assert data['id'] == 1


# ----- TEST MESSAGE REQUESTS ----- #
def test_create_post():
    """Check if message is correctly added to database and if predictions are fine"""
    response = client.post(
        "/clients/",
        json={"first_name": "Dupont", "last_name": "Gérard", "mail": "g.dupont@gmail.com", "phone": "0655555555"}
    )

    data = response.json()
    user_id = data['id']

    response = client.post(
        f'/clients/{user_id}/post/',
        json={"text": "I'm feeling happy today !"}
    )

    assert response.status_code == 200
    data = response.json()
    assert data['text'] == "I'm feeling happy today !"
    assert "id" in data
    assert data['date_created'] == dt.datetime.today().strftime('%Y-%m-%d')
    assert data["sentiment"] == "Joy"
    assert data['percent_joy'] + data['percent_anger'] + data['percent_fear'] + data['percent_sadness'] == 1


def test_update_post():
    """Check if message is existing message if correctly updated and its sentiment prediction too"""
    user_id = 1

    response = client.put(
        f"/clients/{user_id}/post/",
        json={"text": "Weather is so sad ..."}
    )
    data = response.json()
    assert data['text'] == "Weather is so sad ..."
    assert data['date_last_updated'] == dt.datetime.today().strftime('%Y-%m-%d')


