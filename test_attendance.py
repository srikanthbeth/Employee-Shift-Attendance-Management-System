from .conftest import client


def test_get_attendance():

    response = client.get("/attendance")

    assert response.status_code in [200, 401, 403]