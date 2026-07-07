from .conftest import client


def test_get_employees():

    response = client.get("/employees")

    assert response.status_code in [200, 401, 403]