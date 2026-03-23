import pytest
from tests.data.api_client import APIclient
from endpoints import api_requests


@pytest.fixture
def client():
    client = APIclient()
    client.auth()
    return client

@pytest.fixture
def booking_id():
    response = api_requests.create_booking()
    data = response.json()
    return data["bookingid"]

@pytest.fixture
def updated_booking(client, booking_id):
    response = api_requests.update_booking()
    data = response.json()