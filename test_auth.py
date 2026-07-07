from .conftest import client


def test_register():

    response = client.post(
        "/auth/register",
        json={
            "username": "admin",
            "email": "admin@test.com",
            "password": "admin123",
            "role": "Admin"
        }
    )

    assert response.status_code in [200, 201]


def test_login():

    response = client.post(
        "/auth/login",
        json={
            "username": "admin",
            "password": "admin123"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()