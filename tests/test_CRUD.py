import pytest
from endpoints import api_requests
from tests.data import client_data

def test_auth(client):
    assert client.token is not None

def test_auth_response(client):
    response = client.auth()

    assert response.status_code == 200
    assert "token" in response.json()

def test_crud_booking(client):
    create_response = api_requests.create_booking()
    assert create_response.status_code == 200

    create_data = create_response.json()
    booking_id = create_data["bookingid"]

    assert create_data["booking"]["firstname"] == client_data.payload["firstname"]

    update_response = api_requests.update_booking(client.session, booking_id)
    assert update_response.status_code == 200

    update_data = update_response.json()
    assert update_data["firstname"] == client_data.update_payload["firstname"]
    assert update_data["lastname"] == client_data.update_payload["lastname"]

    get_response = api_requests.get_booking(client.session, booking_id)
    assert get_response.status_code == 200

    get_data = get_response.json()
    assert get_data == client_data.update_payload

    delete_response = api_requests.delete_booking(client.session, booking_id)
    assert delete_response.status_code == 201

    get_after_delete = api_requests.get_booking(client.session, booking_id)
    assert get_after_delete.status_code == 404




