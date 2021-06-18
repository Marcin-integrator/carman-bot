from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get(
        '/', headers={'content-type': 'text/html; charset=uft-8'})
    assert response.status_code == 200
    assert b'Welcome to Cartman bot' in response.content
    response = client.get('/static/css/style3.css')
    assert response.status_code == 200


def test_page_about():
    response = client.get(
        '/page/about', headers={'content-type': 'text/html; charset=uft-8'})
    assert response.status_code == 200
    assert b'About' in response.content


def test_unsplash():
    response = client.get("/lines",
                          headers={"content-type": "text/html; charset=utf-8"})
    assert response.status_code == 200
    assert b"Lines" in response.content
