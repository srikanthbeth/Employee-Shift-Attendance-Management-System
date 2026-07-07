from .conftest import client


def test_get_shifts():

    response = client.get("/shifts")

    assert response.status_code in [200, 401, 403]